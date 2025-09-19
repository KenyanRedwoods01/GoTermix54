# gotermix54/commands/dev.py
import click
import os
from pathlib import Path
from ..ai import AIRouter
from ..context import ContextManager

@click.group()
def dev():
    """🏗️  Project generation & code editing"""
    pass

@dev.command()
@click.argument('name')
@click.option('--stack', '-s', help='Comma-separated tech stack')
@click.pass_context
def create_project_interactive(context, ai):
    from questionary import text, select, confirm

    console = Console()
    console.print(Panel("🚀 Project Creator Wizard", style="bold green"))

    name = text("Project name:").ask()
    stack = text("Tech stack (comma separated):", default="python,fastapi").ask()
    auth = select("Authentication:", choices=["None", "JWT", "OAuth2", "Session"]).ask()
    deploy = confirm("Include deployment config?").ask()

    console.print(f"[bold]Creating [cyan]{name}[/cyan] with [yellow]{stack}[/yellow]...[/bold]")

    # ... reuse your existing create logic here
    # Then show success panel
    console.print(Panel(f"✅ Project '{name}' created successfully!", style="bold green"))
    console.input("[dim]Press Enter to return...[/dim]")

def edit_file_interactive(file_path):
    from questionary import text
    from ..ai import AIRouter
    console = Console()

    ai = AIRouter()
    content = file_path.read_text()

    console.print(Panel(f"✍️  Editing: {file_path}", style="bold yellow"))
    instruction = text("What should I change?").ask()

    with console.status("[bold blue]AI is refactoring...", spinner="dots"):
        prompt = f"Edit this file: {instruction}\n\n{content}\n\nOutput ONLY the new content."
        new_content = ai.route(prompt, mode="coding")

    console.print("\n[bold]Preview Changes:[/bold]")
    from rich.syntax import Syntax
    diff = "\n".join([
        f"  {line}" if line.startswith(" ") else
        f"[green]+{line}[/green]" if line.startswith("+") else
        f"[red]-{line}[/red]"
        for line in difflib.unified_diff(
            content.splitlines(),
            new_content.splitlines(),
            lineterm=""
        )
    ][2:])  # Skip header

    console.print(Syntax(diff, "diff", theme="monokai"))

    if confirm("Apply changes?").ask():
        file_path.write_text(new_content)
        console.print("[bold green]✅ File updated![/bold green]")
    else:
        console.print("[dim]Cancelled.[/dim]")
def create(ctx, name, stack):
    """🚀 Create new project"""
    ai = ctx.obj['ai']
    context = ctx.obj['context']

    tech_list = stack.split(",") if stack else ["python"]
    prompt = f"""
    Generate a complete project structure for '{name}' using {', '.join(tech_list)}.
    Output as a JSON object with keys: "files" (list of {{path, content}}), "instructions" (setup steps).
    No markdown, no explanation.
    """

    response = ai.route(prompt, mode="coding")
    try:
        import json
        data = json.loads(response)
        
        # Create files
        for file in data.get("files", []):
            path = Path(file["path"])
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(file["content"])
            click.echo(f"✅ Created {file['path']}")
            context.add_file(file["path"])

        # Show instructions
        click.echo("\n📘 Instructions:")
        for step in data.get("instructions", []):
            click.echo(f"  → {step}")

        context.set_goal(f"Project {name} with stack {stack}")
        context.save()

    except Exception as e:
        click.echo(f"❌ Failed to parse AI response: {e}")
        click.echo(response)

@dev.command()
@click.argument('file')
@click.option('--instruction', '-i', required=True, help='What to change')
@click.pass_context
def edit(ctx, file, instruction):
    """✍️ Edit file with AI"""
    ai = ctx.obj['ai']
    path = Path(file)
    if not path.exists():
        click.echo(f"❌ File {file} not found")
        return

    content = path.read_text()
    prompt = f"""
    Edit this file according to instruction: "{instruction}"

    FILE: {file}
    CONTENT:
    {content}

    Output ONLY the new file content. No explanations.
    """

    new_content = ai.route(prompt, mode="coding")
    if click.confirm(f"Replace content of {file}?"):
        path.write_text(new_content)
        click.echo(f"✅ Updated {file}")
