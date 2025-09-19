# gotermix54/commands/sys.py
import click
from ..core.executor import run_shell_command
from ..ai import AIRouter

@click.group()
def sys():
    """🐧 Execute & explain system commands"""
    pass

@sys.command()
@click.argument('command', nargs=-1)
@click.pass_context
def run(ctx, command):
    """▶️ Run native shell command"""
    cmd_str = " ".join(command)
    click.echo(f"→ Running: {cmd_str}")
    _, _, code = run_shell_command(cmd_str)
    if code != 0:
        click.echo(f"⚠️  Command exited with code {code}")

@sys.command()
@click.argument('query', nargs=-1)
@click.pass_context
def explain(ctx, query):
    """🧠 Explain system command or output"""
    ai = AIRouter()
    query_str = " ".join(query)
    prompt = f"You are a Linux system expert. Explain this command or concept to a developer: {query_str}"
    response = ai.route(prompt, mode="reasoning")
    click.echo(response)

@sys.command()
@click.argument('issue')
@click.pass_context
def fix(ctx, issue):
    """🔧 AI-assisted system fix"""
    ai = AIRouter()
    prompt = f"""
    You are an AI system administrator. Suggest a SAFE Linux/Termux command to fix this issue: "{issue}".
    Output ONLY the command, no explanation. If unsure, output "echo 'No safe fix found'".
    """
    cmd = ai.route(prompt, mode="reasoning")
    click.echo(f"💡 Suggested: {cmd}")
    if click.confirm("Execute?"):
        run_shell_command(cmd)
