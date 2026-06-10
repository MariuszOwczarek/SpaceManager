from textual.containers import Horizontal, Vertical
from ui.panels.planet_panel import PlanetPanel


class HomeworldLayout(Vertical):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def on_mount(self):
        planet_panel = self.query_one(
            PlanetPanel
        )
        planet_panel.refresh_planet_style()
        planet_panel.refresh()

    def compose(self):
        with Horizontal(id="middle"):
            yield PlanetPanel(
                self.game,
                id="planet_panel"
            )

