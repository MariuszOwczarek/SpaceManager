from textual.widgets import Static
from rich.panel import Panel


class CommandsPanel(Static):
    def render(self):
        help_text = """
        [bold cyan]COMMANDS[/bold cyan]
        ACTIONS.  : move, buy, sell, build, load, store, end, exit
        PLANETS   : mars, venus, supiter, saturn, mercury
        BUILDINGS : hospital, school, factory, barracks
        """
        return Panel(
            help_text,
            title="[bold blue]COMMAND HELP[/bold blue]",
            border_style="blue"
        )
