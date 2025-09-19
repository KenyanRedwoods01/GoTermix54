# gotermix54/ui.py
import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.align import Align
from rich.text import Text
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.styles import Style
from prompt_toolkit.filters import Condition
from .commands.learn import start_interactive_tutor
from .commands.dev import create_project_interactive
from .ai import AIRouter
from .context import ContextManager
from .core.monitor import SystemMonitor

console = Console()

class GoTermixUI:
    def __init__(self):
        self.ai = AIRouter()
        self.context = ContextManager()
        self.monitor = SystemMonitor()
        self.running = True
        self.mode = "menu"  # menu, chat, explore, monitor
        self.chat_history = []
        self.selected_menu = 0
        self.menu_items = [
            "🚀 Create Project",
            "🧠 AI Chat & Explain",
            "📂 File Explorer",
            "📊 System Monitor",
            "📚 Interactive Tutor",
            "⚙️  Settings",
            "🚪 Exit"
        ]

    def render_menu(self):
        layout = Layout()
        layout.split_column(
            Layout(self.render_header(), size=3),
            Layout(self.render_menu_panel(), size=10),
            Layout(self.render_footer(), size=3)
        )
        return layout

    def render_header(self):
        title = Text("GoTermix54", style="bold cyan")
        subtitle = Text("AI-Powered Dev Terminal • Termux Ready", style="green")
        panel = Panel(
            Align.center(f"{title}\n{subtitle}"),
            border_style="bright_blue",
            title="🌟 Welcome",
            title_align="left"
        )
        return panel

    def render_menu_panel(self):
        table = Table(show_header=False, box=None, padding=(0, 2))
        for i, item in enumerate(self.menu_items):
            if i == self.selected_menu:
                table.add_row(f"> [bold yellow]{item}[/bold yellow]")
            else:
                table.add_row(f"  {item}")
        return Panel(table, title="🧭 Navigation", border_style="blue")

    def render_footer(self):
        tips = [
            "↑↓: Navigate • Enter: Select • q: Quit • c: Quick Chat",
            "💡 Pro Tip: Type '!' then command to run shell (e.g !ls)"
        ]
        return Panel("\n".join(tips), style="dim")

    def render_chat(self):
        messages = []
        for msg in self.chat_history[-10:]:
            if msg['role'] == 'user':
                messages.append(f"[bold green]You:[/bold green] {msg['content']}")
            else:
                messages.append(f"[bold blue]AI:[/bold blue] {msg['content']}")
        
        chat_content = "\n".join(messages) if messages else "[dim]No messages yet. Ask anything![/dim]"
        input_area = "\n" + ("_" * 50) + "\n[bold yellow]Type your question (ESC to exit chat):[/bold yellow]"

        layout = Layout()
        layout.split_column(
            Layout(self.render_header(), size=3),
            Layout(Panel(chat_content, title="💬 AI Chat", border_style="green"), ratio=4),
            Layout(Panel(input_area, border_style="yellow"), size=3)
        )
        return layout

    def run(self):
        console.clear()
        with Live(self.render_menu(), refresh_per_second=4, console=console) as live:
            while self.running:
                key = self.get_key()
                if key == 'q':
                    break
                elif key == 'up':
                    self.selected_menu = (self.selected_menu - 1) % len(self.menu_items)
                elif key == 'down':
                    self.selected_menu = (self.selected_menu + 1) % len(self.menu_items)
                elif key == 'enter':
                    self.handle_selection()
                elif key == 'c':
                    self.mode = "chat"
                    self.run_chat_mode(live)
                    self.mode = "menu"
                live.update(self.render_menu())

    def run_chat_mode(self, live):
        console.show_cursor(True)
        while True:
            console.print("\n[bold yellow]You:[/bold yellow] ", end="")
            user_input = input()
            if user_input.lower() in ['exit', 'quit', 'back', '']:
                break
            if user_input.startswith('!'):
                # Run shell command
                cmd = user_input[1:].strip()
                console.print(f"[dim]→ Running: {cmd}[/dim]")
                from .core.executor import run_shell_command
                out, err, code = run_shell_command(cmd, capture_output=True)
                if code == 0:
                    console.print(f"[green]{out}[/green]")
                else:
                    console.print(f"[red]{err}[/red]")
                continue

            self.chat_history.append({"role": "user", "content": user_input})
            with console.status("[bold blue]AI is thinking...", spinner="dots"):
                response = self.ai.route(user_input, mode="reasoning")
            self.chat_history.append({"role": "assistant", "content": response})
            console.print(f"[bold blue]AI:[/bold blue] {response}")
        console.show_cursor(False)

    def handle_selection(self):
        selection = self.selected_menu
        if selection == 0:  # Create Project
            create_project_interactive(self.context, self.ai)
        elif selection == 1:  # AI Chat
            self.mode = "chat"
            with Live(self.render_chat(), refresh_per_second=1, console=console) as live:
                self.run_chat_mode(live)
        elif selection == 2:  # File Explorer
            self.launch_file_explorer()
        elif selection == 3:  # System Monitor
            self.monitor.display_live()
        elif selection == 4:  # Tutor
            start_interactive_tutor(self.ai)
        elif selection == 5:  # Settings
            self.show_settings()
        elif selection == 6:  # Exit
            self.running = False

    def launch_file_explorer(self):
        from .utils.file_explorer import FileExplorer
        fe = FileExplorer()
        fe.run()

    def show_settings(self):
        console.print(Panel("⚙️  Settings Panel (Coming Soon)", border_style="yellow"))
        console.input("[dim]Press Enter to return...[/dim]")

    def get_key(self):
        # Simple key capture for Termux/Linux
        import tty, termios, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x1b':  # Arrow keys start with ESC
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A': return 'up'
                    elif ch3 == 'B': return 'down'
            elif ch == '\r': return 'enter'
            elif ch == 'q': return 'q'
            elif ch == 'c': return 'c'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None
