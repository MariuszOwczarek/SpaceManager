from textual.widgets import Static
from rich.panel import Panel
from rich.table import Table
from config.facilities import FACILITIES
from systems.facilities import (get_building_credit_cost,
                                get_building_resource_cost)


class FacilitiesPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        planet = self.game.planets[self.game.current_planet]
        table = Table(expand=True)
        table.add_column("BUILDING")
        table.add_column("COUNT")
        table.add_column("COST")
        table.add_column("RESOURCES")
        for building_key in FACILITIES:
            resource_costs = (
                get_building_resource_cost(FACILITIES, building_key, planet)
            )
            resource_text = " | ".join(
                f"{resource[:4].upper()}:{amount}"
                for resource, amount in (
                    resource_costs.items()
                )
            )

            credit_cost = (
                get_building_credit_cost(FACILITIES, building_key, planet)
            )

            table.add_row(
                building_key.upper(),
                str(planet.buildings[building_key]),
                str(credit_cost),
                resource_text
            )
        planet_color = (planet.definition.color)
        return Panel(table,
                     title=f"[{planet_color}]"
                     f"FACILITY PROGRESS"
                     f"[/{planet_color}]",
                     border_style=planet_color)
