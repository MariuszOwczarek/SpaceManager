from textual.app import App
from textual.widgets import Input
from textual.containers import Horizontal
from core.game_state import GameState
from commands.move import handle_move
from commands.buy import handle_buy
from commands.sell import handle_sell
from commands.build import handle_build
from commands.load import handle_load
from commands.store import handle_store
from commands.turn_end import handle_turn_end
from ui.layouts.foreign_layout import ForeignLayout
from ui.layouts.homeworld_layout import HomeworldLayout
from ui.layouts.base_layout import BaseLayout
from utils.ui import fail, add_log
from textual.containers import Container
from ui.shell.logs_panel import LogsPanel
from ui.shell.header_panel import HeaderPanel
from ui.shell.cargo_panel import CargoPanel
from ui.shell.warehouse_panel import WarehousePanel
from ui.shell.intel_panel import IntelPanel
from ui.shell.command_panel import CommandsPanel


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

    # =========================================
    # ROOT UI
    # =========================================

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
            id="main_content"
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

    # =========================================
    # INITIALIZE
    # =========================================

    async def on_mount(self):
        await self.load_layout()

    # =========================================
    # DYNAMIC LAYOUT
    # =========================================

    async def load_layout(self):
        container = self.query_one(
            "#main_content"
        )
        await container.remove_children()
        planet = self.game.planets[
            self.game.current_planet
        ]

        if planet.definition.is_homeworld:
            await container.mount(
                HomeworldLayout(
                    self.game
                )
            )
        else:
            await container.mount(
                ForeignLayout(
                    self.game
                )
            )

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
        elif action in ["l", "load"]:
            handle_load(
                game=self.game,
                app=self,
                parts=parts
            )
        elif action in ["store"]:
            handle_store(
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
            add_log(self.game, "move mars | buy iron 10 | sell gold 5")
        else:
            add_log(self.game, "INVALID COMMAND")

    def refresh_all(self):
        self.query_one(HeaderPanel).refresh()
        self.query_one(CargoPanel).refresh()
        self.query_one(CommandsPanel).refresh()
        self.query_one(WarehousePanel).refresh()
        self.query_one(LogsPanel).refresh()
        self.query_one(IntelPanel).refresh()

        layouts = list(self.query(BaseLayout))
        if layouts:
            layouts[0].refresh_all()


# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    app = StarManager()
    app.run()
