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
