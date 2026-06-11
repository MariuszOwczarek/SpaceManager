from textual.widgets import Static
from rich.panel import Panel
from systems.inventory.storage import used_storage, free_storage


class WarehousePanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        cargo = []
        planet = self.game.planets[self.game.current_planet]
        resources = planet.storage
        for resource, amount in resources.items():
            if amount > 0:
                cargo.append(f"{resource.upper()}:{amount}")
        if cargo:
            cargo_planet_text = " | ".join(cargo)
        else:
            cargo_planet_text = "[dim]NO CARGO[/dim]"

        text = (
            f"[bold red]STORAGE:[/bold red] "
            f"{used_storage(planet, resources)}/"
            f"{planet.storage_capacity} "
            f"[bold red]FREE:[/bold red] "
            f"{free_storage(planet, resources)}\n"
            f"{cargo_planet_text}\n\n\n"
        )
        title_inside = "WAREHOUSE"
        return Panel(
            text,
            title=f"[bold red]{title_inside}[/bold red]",
            border_style="red"
        )
