from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Input
from ui.panels import (PlanetPanel, LogsPanel, IntelPanel, HeaderPanel,
                       MarketPanel, StatusPanel, CommandsPanel, BuildingsPanel,
                       CargoPanel)
from core.state import GameState
from commands.move import handle_move
from commands.buy import handle_buy
from commands.sell import handle_sell
from commands.build import handle_build
from commands.turn_end import handle_turn_end
from utils.ui import fail


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
        height: 1.5fr;
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
    #planet_panel{
        padding: 1;
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

    # =====================================================
    # UI
    # =====================================================
    def on_mount(self):
        planet_panel = self.query_one(
            PlanetPanel
        )

        planet_panel.refresh_planet_style()

    def compose(self) -> ComposeResult:
        with Horizontal(id="top"):
            yield HeaderPanel(self.game, id="header")
            yield CargoPanel(self.game, id="cargo")
            yield IntelPanel(self.game, id="intel")

        with Horizontal(id="middle"):
            yield PlanetPanel(self.game, id="planet_panel")

        with Horizontal(id="bottom_input"):
            yield Input(placeholder="COMMAND...")

        with Horizontal(id="bottom_panels"):
            yield CommandsPanel(id="commands")
            yield LogsPanel(self.game, id="logs")

    # =====================================================
    # REFRESH
    # =====================================================
    def refresh_all(self):
        planet_panel = self.query_one(PlanetPanel)
        planet_panel.refresh_planet_style()
        self.query_one(HeaderPanel).refresh()
        self.query_one(CargoPanel).refresh()
        self.query_one(LogsPanel).refresh()
        self.query_one(PlanetPanel).refresh()
        self.query_one(StatusPanel).refresh()
        self.query_one(MarketPanel).refresh()
        self.query_one(BuildingsPanel).refresh()
        self.query_one(IntelPanel).refresh()

    # =====================================================
    # INPUT
    # =====================================================
    def on_input_submitted(self, event: Input.Submitted):
        command = event.value.lower()
        event.input.value = ""
        self.process_command(command)

    # =====================================================
    # COMMANDS
    # =====================================================
    def process_command(self, command):
        parts = command.split()

        if not parts:
            return fail(
                game=self.game,
                app=self,
                message="PLEASE PROVDE COMMAND FROM A LIST"
            )

        action = parts[0].lower()

        if action in ["x", "exit"]:
            self.exit()

        elif action in ["m", "move"]:
            handle_move(
                game=self.game,
                app=self,
                parts=parts
            )

        elif action in ["b", "buy"]:
            handle_buy(
                game=self.game,
                app=self,
                parts=parts
            )

        elif action in ["s", "sell"]:
            handle_sell(
                game=self.game,
                app=self,
                parts=parts
            )

        elif action == "build":
            handle_build(
                game=self.game,
                app=self,
                parts=parts
            )

        elif action in ["e", "end"]:
            handle_turn_end(
                game=self.game,
                app=self
            )

        elif action == "help":
            self.game.add_log("move mars | buy iron 10 | sell gold 5")

        else:
            self.game.add_log("INVALID COMMAND")

        self.refresh_all()


# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    app = StarManager()
    app.run()
