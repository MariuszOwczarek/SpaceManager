from textual.widgets import Static
from rich.panel import Panel


class CommandsPanel(Static):
    def render(self):
        help_text = """
        [bold cyan]COMMANDS[/bold cyan]
        ACTIONS:   | move     | buy    | sell    | build   | end     | exit
        PLANETS:   | Mars     | Venus  | Jupiter | Saturn  | Mercury
        BUILDINGS: | Hospital | School | Factory | Barracks
        """
        return Panel(
            help_text,
            title="[bold blue]COMMAND HELP[/bold blue]",
            border_style="blue"
        )
