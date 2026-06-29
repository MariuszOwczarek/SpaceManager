from textual.containers import Horizontal
from ui.panels.planet_panel import PlanetPanel
from ui.layouts.base_layout import BaseLayout
from ui.panels.facilities_panel import FacilitiesPanel
from ui.panels.market_panel import MarketPanel
from ui.panels.status_panel import StatusPanel
from textual.containers import Container


class HomeworldLayout(BaseLayout):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def compose(self):
        with Horizontal(id="main_content"):
            yield Container(
                id="workspace_content"
            )

    def refresh_all(self):
        # planet_panel = self.query_one(
        #    PlanetPanel
        # )
        # planet_panel.refresh_planet_style()
        refreshables = [
            # planet_panel,
            self.query_one(StatusPanel),
            self.query_one(MarketPanel),
            self.query_one(FacilitiesPanel),
            ]
        for widget in refreshables:
            widget.refresh()
