# gotermix54/core/monitor.py
import psutil
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout

class SystemMonitor:
    def __init__(self):
        self.console = Console()

    def get_stats(self):
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return {
            "cpu": cpu,
            "memory_percent": mem.percent,
            "memory_used": mem.used / 1024**3,
            "memory_total": mem.total / 1024**3,
            "disk_percent": disk.percent,
            "disk_used": disk.used / 1024**3,
            "disk_total": disk.total / 1024**3,
            "processes": len(psutil.pids())
        }

    def render(self, stats):
        layout = Layout()
        layout.split_column(
            Layout(self.render_header(), size=3),
            Layout(self.render_stats_table(stats), size=8),
            Layout(self.render_process_list(), size=10),
            Layout(self.render_footer(), size=3)
        )
        return layout

    def render_header(self):
        return Panel("📊 Real-Time System Monitor", style="bold magenta")

    def render_stats_table(self, stats):
        table = Table(title="Resource Usage", show_header=True, header_style="bold cyan")
        table.add_column("Resource", style="dim")
        table.add_column("Usage", style="bold")
        table.add_column("Value")

        table.add_row("CPU", f"{stats['cpu']}%", self.get_bar(stats['cpu']))
        table.add_row("Memory", f"{stats['memory_percent']}%", self.get_bar(stats['memory_percent']))
        table.add_row("Disk", f"{stats['disk_percent']}%", self.get_bar(stats['disk_percent']))
        table.add_row("Processes", str(stats['processes']), "")

        return table

    def get_bar(self, percent):
        from rich.progress import Progress, BarColumn
        from io import StringIO
        from rich.console import Console
        console = Console(file=StringIO(), force_terminal=True)
        with console.capture() as capture:
            console.print(f"[{'█' * int(percent/5)}{'░' * (20 - int(percent/5))}]")
        return capture.get()

    def render_process_list(self):
        procs = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                if pinfo['cpu_percent'] > 0.1 or (pinfo['memory_percent'] or 0) > 1.0:
                    procs.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        procs = sorted(procs, key=lambda x: x.get('cpu_percent', 0), reverse=True)[:5]

        table = Table(title="Top Processes", show_header=True, header_style="bold yellow")
        table.add_column("PID", style="dim")
        table.add_column("Name")
        table.add_column("CPU%", justify="right")
        table.add_column("MEM%", justify="right")

        for p in procs:
            table.add_row(
                str(p['pid']),
                p['name'][:20],
                f"{p.get('cpu_percent', 0):.1f}%",
                f"{p.get('memory_percent', 0):.1f}%"
            )

        return Panel(table, border_style="yellow")

    def render_footer(self):
        return Panel("q: Quit | r: Refresh", style="dim")

    def display_live(self):
        with Live(self.render(self.get_stats()), refresh_per_second=1, console=Console()) as live:
            while True:
                key = self.get_key()
                if key == 'q':
                    break
                live.update(self.render(self.get_stats()))

    def get_key(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == 'q':
                return 'q'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None
