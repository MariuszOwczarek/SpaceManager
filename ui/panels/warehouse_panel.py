from textual.widgets import Static
from rich.panel import Panel


class WarehousePanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        cargo = []
        planet = self.game.planets[self.game.current_planet]
        for resource, amount in planet.storage.items():
            if amount > 0:
                cargo.append(f"{resource.upper()}:{amount}")
        if cargo:
            cargo_planet_text = " | ".join(cargo)
        else:
            cargo_planet_text = "[dim]NO CARGO[/dim]"

        text = (
            f"[bold red]STORAGE:[/bold red] "
            f"{planet.used_storage()}/"
            f"{planet.storage_capacity} "
            f"[bold red]FREE:[/bold red] "
            f"{planet.free_storage()}\n"
            f"{cargo_planet_text}\n\n\n"
        )
        title_inside = "WAREHOUSE"
        return Panel(
            text,
            title=f"[bold red]{title_inside}[/bold red]",
            border_style="red"
        )
