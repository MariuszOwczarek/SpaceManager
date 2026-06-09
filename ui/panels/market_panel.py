from textual.widgets import Static
from rich.panel import Panel
from rich.table import Table
from config.resources import RESOURCES


class MarketPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        planet = self.game.planets[self.game.current_planet]
        table = Table(expand=True)
        table.add_column("RESOURCES")
        table.add_column("AVAILABLE")
        table.add_column("PRICE")
        table.add_column("WEIGHT")

        for resource_key, market_item in planet.market.items():
            resource = RESOURCES[resource_key]
            price = market_item.price
            stock = market_item.stock
            if price < 30:
                color = "green"
            elif price < 100:
                color = "yellow"
            else:
                color = "red"

            table.add_row(
                resource.name.upper(),
                str(stock),
                f"[{color}]" f"{price}" f"[/{color}]",
                str(resource.weight),
            )
        planet_color = (planet.definition.color)
        return Panel(table,
                     title=f"[{planet_color}]"
                     f"MARKET PLACE"
                     f"[/{planet_color}]",
                     border_style=planet_color)
