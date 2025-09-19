# gotermix54/utils/file_explorer.py
import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.live import Live
from rich.layout import Layout

class FileExplorer:
    def __init__(self):
        self.console = Console()
        self.current_path = Path.cwd()
        self.selected_index = 0
        self.items = []

    def scan_directory(self):
        self.items = []
        # Add ".." for up
        self.items.append(".. (Parent Directory)")
        # Add dirs
        for item in sorted(self.current_path.iterdir()):
            if item.is_dir():
                self.items.append(f"📁 {item.name}")
        # Add files
        for item in sorted(self.current_path.iterdir()):
            if item.is_file():
                self.items.append(f"📄 {item.name}")

    def render(self):
        layout = Layout()
        layout.split_column(
            Layout(self.render_header(), size=3),
            Layout(self.render_file_list(), ratio=1),
            Layout(self.render_footer(), size=3)
        )
        return layout

    def render_header(self):
        return Panel(f"📂 File Explorer — {self.current_path}", style="bold blue")

    def render_file_list(self):
        tree = Tree("Contents")
        for i, item in enumerate(self.items):
            if i == self.selected_index:
                tree.add(f"[bold yellow]> {item}[/bold yellow]")
            else:
                tree.add(f"  {item}")
        return Panel(tree, border_style="cyan")

    def render_footer(self):
        return Panel("↑↓: Navigate • Enter: Open/CD • q: Quit • e: Edit (if file)", style="dim")

    def run(self):
        self.scan_directory()
        with Live(self.render(), refresh_per_second=4, console=self.console) as live:
            while True:
                key = self.get_key()
                if key == 'q':
                    break
                elif key == 'up':
                    self.selected_index = (self.selected_index - 1) % len(self.items)
                elif key == 'down':
                    self.selected_index = (self.selected_index + 1) % len(self.items)
                elif key == 'enter':
                    self.handle_selection()
                    self.scan_directory()
                elif key == 'e' and self.selected_index > 0:
                    self.edit_file()
                live.update(self.render())

    def handle_selection(self):
        if self.selected_index == 0:
            self.current_path = self.current_path.parent
        else:
            item_name = self.items[self.selected_index].replace("📁 ", "").replace("📄 ", "")
            new_path = self.current_path / item_name
            if new_path.is_dir():
                self.current_path = new_path
            elif new_path.is_file():
                self.console.print(f"[dim]📄 Selected: {new_path}[/dim]")

    def edit_file(self):
        if self.selected_index == 0:
            return
        item_name = self.items[self.selected_index].replace("📁 ", "").replace("📄 ", "")
        file_path = self.current_path / item_name
        if file_path.is_file():
            from ..commands.dev import edit_file_interactive
            edit_file_interactive(file_path)

    def get_key(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A': return 'up'
                    elif ch3 == 'B': return 'down'
            elif ch == '\r': return 'enter'
            elif ch == 'q': return 'q'
            elif ch == 'e': return 'e'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None
