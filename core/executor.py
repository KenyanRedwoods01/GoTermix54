# gotermix54/core/executor.py
import subprocess
import sys
from rich.console import Console

console = Console()

def run_shell_command(cmd, shell=True, capture_output=False):
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=shell, text=True, capture_output=True)
            return result.stdout, result.stderr, result.returncode
        else:
            result = subprocess.run(cmd, shell=shell)
            return None, None, result.returncode
    except Exception as e:
        console.print(f"[red]Execution failed: {e}[/red]")
        return None, str(e), -1
