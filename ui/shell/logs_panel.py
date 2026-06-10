from textual.widgets import Static
from rich.panel import Panel


class LogsPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        if self.game.logs:
            logs = "\n".join(f"> {log}" for log in self.game.logs)
        else:
            logs = "[dim]NO LOGS[/dim]"
        return Panel(logs,
                     title="[green]ACTION LOGS[/green]",
                     border_style="green")
