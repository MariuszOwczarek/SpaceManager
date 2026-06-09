from textual.containers import Horizontal, Vertical
from textual.widgets import Input
from ui.panels.cargo_panel import CargoPanel
from ui.panels.warehouse_panel import WarehousePanel
from ui.panels.planet_panel import PlanetPanel
from ui.panels.logs_panel import LogsPanel
from ui.panels.intel_panel import IntelPanel
from ui.panels.header_panel import HeaderPanel
from ui.panels.command_panel import CommandsPanel


class HomeworldLayout(Vertical):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def on_mount(self):
        planet_panel = self.query_one(
            PlanetPanel
        )
        planet_panel.refresh_planet_style()

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

        with Horizontal(id="middle"):
            yield PlanetPanel(
                self.game,
                id="planet_panel"
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

    def refresh_all(self):
        planet_panel = self.query_one(PlanetPanel)
        planet_panel.refresh_planet_style()
        refreshables = [
            HeaderPanel,
            CargoPanel,
            WarehousePanel,
            LogsPanel,
            PlanetPanel,
            IntelPanel
        ]
        for widget_type in refreshables:
            widgets = self.query(
                widget_type
            )

            if widgets:
                widgets.first().refresh()
