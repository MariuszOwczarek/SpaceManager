from rich.table import Table
from textual.widgets import Static
from rich.panel import Panel


class StatusPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        planet = self.game.planets[self.game.current_planet]
        table = Table(expand=True)
        table.add_column("ATTRIBUTE")
        table.add_column("VALUE")
        table.add_row("Max Population", str(planet.max_population))
        table.add_row("Population", str(planet.population))
        table.add_row("Health", str(planet.health))
        table.add_row("Happiness", str(planet.happiness))
        table.add_row("Safety", str(planet.safety))
        table.add_row("Soldiers", str(planet.soldiers))
        planet_color = (planet.definition.color)

        return Panel(table,
                     title=f"[{planet_color}]"
                     f"CURRENT STATUS"
                     f"[/{planet_color}]",
                     border_style=planet_color)
