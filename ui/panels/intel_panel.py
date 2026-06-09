from textual.widgets import Static
from rich.panel import Panel
from rich.table import Table
from config.resources import RESOURCES


class IntelPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        table = Table(expand=True)
        table.add_column("RESOURCES")
        for planet_name in self.game.market_memory.keys():
            planet = self.game.planets[planet_name]
            short_name = planet.definition.shortcut
            age = self.game.turn - self.game.market_memory[planet_name]["turn"]
            table.add_column(f"{short_name} {age}T")

        for resource_key in RESOURCES:
            row = [resource_key.upper()]
            for planet_name in self.game.market_memory.keys():
                prices = (self.game.market_memory[planet_name]["prices"])
                price = prices.get(resource_key)
                if price is None:
                    row.append("[dim]---[/dim]")
                else:
                    row.append(str(price))
            table.add_row(*row)
        return Panel(
            table,
            title="[magenta]MARKET INTEL[/magenta]",
            border_style="magenta"
        )
