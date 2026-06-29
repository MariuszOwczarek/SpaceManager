from textual.containers import Horizontal, Vertical
from ui.panels.status_panel import StatusPanel
from ui.panels.market_panel import MarketPanel
from ui.panels.facilities_panel import FacilitiesPanel


class PlanetPanel(Vertical):

    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def compose(self):
        with Horizontal(classes="planet_content"):
            yield StatusPanel(
                self.game,
                id="status"
            )

            yield MarketPanel(
                self.game,
                id="market"
            )

            yield FacilitiesPanel(
                self.game,
                id="buildings"
            )

    def refresh_planet_style(self):
        planet = self.game.planets[self.game.current_planet]
        definition = planet.definition

        self.border_title = (
            f"[{definition.color}]"
            f"PLANET "
            f"{definition.name.upper()} "
            f"COMMAND CENTER "
            f"[/]"
            f"([dim]"
            f"{definition.type.upper()}"
            f"[/dim])"
        )

        self.styles.border = (
            "solid",
            definition.color
        )

        self.refresh()
