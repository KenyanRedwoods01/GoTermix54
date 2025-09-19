# gotermix54/cli.py
import click
from .config import load_config, save_global_config
from .context import ContextManager
from .ai import AIRouter

# Import command groups
from .commands import sys_cmd, dev_cmd, ops_cmd, pkg_cmd, learn_cmd

@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.option('--ai-model', type=click.Choice(['mistral', 'codestral', 'auto']), default=None)
@click.pass_context
def cli(ctx, verbose, ai_model):
    """🚀 GoTermix54 — AI-Powered Dev CLI for Termux & Linux"""
    ctx.ensure_object(dict)
    config = load_config()
    if verbose:
        config['system']['verbose'] = True
    if ai_model:
        config['ai']['model'] = ai_model
    ctx.obj['config'] = config
    ctx.obj['context'] = ContextManager()
    ctx.obj['ai'] = AIRouter()

# Register command groups
cli.add_command(sys_cmd.sys)
cli.add_command(dev_cmd.dev)
cli.add_command(ops_cmd.ops)
cli.add_command(pkg_cmd.pkg)
cli.add_command(learn_cmd.learn)

# Root explain command (alias to learn explain)
@cli.command()
@click.argument('query', nargs=-1)
@click.pass_context
def explain(ctx, query):
    """🧠 AI explanation for commands or concepts"""
    ai = ctx.obj['ai']
    query_str = " ".join(query)
    response = ai.route(f"Explain this in simple terms for a developer: {query_str}", mode="reasoning")
    click.echo(response)

if __name__ == '__main__':
    cli(obj={})
