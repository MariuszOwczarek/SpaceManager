from textual.app import App
from textual.widgets import Input
from textual.containers import Horizontal
from app.workspace_manager import load_workspace
from core.game_state import GameState

from textual.containers import Container
from ui.shell.logs_panel import LogsPanel
from ui.shell.header_panel import HeaderPanel
from ui.shell.cargo_panel import CargoPanel
from ui.shell.warehouse_panel import WarehousePanel
from ui.shell.intel_panel import IntelPanel
from ui.shell.command_panel import CommandsPanel
from app.router import process_command
from app.layout_manager import load_layout


class StarManager(App):
    CSS = """
    Screen {
        background: black;
    }
    #top {
        height: 1fr;
        layout: horizontal;
    }
    #middle {
        height: 1.3fr;
        layout: horizontal;
    }
    #bottom_input{
        height: 5;
    }
    #bottom_panels{
        height: 10;
        layout: horizontal;
    }
    #header {
        width: 1fr;
    }
    #commands{
        width: 1fr;
    }
    #logs{
        width: 1fr;
    }
    #cargo {
        width: 1fr;
    }
    #cargo_planet{
        width: 1fr;
    }
    #planet_panel{

        width: 3fr;
    }
    .planet_title{
        height: auto;
        content-align: center middle;
        text-style: bold;
    }
    .planet_content{
        height: auto;
        layout: horizontal;
    }
    #status {
        width: 1fr;
    }
    #market {
        width: 1fr;
    }
    #buildings {
        width: 1fr;
    }
    #intel {
        width: 2fr;
    }
    Static {
        height: 1fr;
        margin-left: 1;
        margin-right: 1;
    }
    Input {
        height: 3;
        border: solid green;
        margin: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.game = GameState()
        self.current_layout = None
        self.current_workspace = None

    def compose(self):
        with Horizontal(id="top"):
            yield HeaderPanel(self.game, id="header")
            yield CargoPanel(self.game, id="cargo")
            yield WarehousePanel(
                self.game,
                id="cargo_planet"
            )
            yield IntelPanel(
                self.game,
                id="intel"
            )

            yield Container(
                id="workspace_content"
            )

        with Horizontal(id="bottom_input"):
            yield Input(
                placeholder="COMMAND..."
            )

        with Horizontal(id="bottom_panels"):
            yield CommandsPanel(
                id="commands"
            )

            yield LogsPanel(
                self.game,
                id="logs"
            )

    async def on_mount(self):
        await load_layout(self)
        self.current_workspace = "overview"
        await load_workspace(self)

    async def on_input_submitted(self, event: Input.Submitted):
        command = event.value.lower()
        event.input.value = ""
        await process_command(self, command)


if __name__ == "__main__":
    app = StarManager()
    app.run()
