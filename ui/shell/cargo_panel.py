from textual.widgets import Static
from rich.panel import Panel
from systems.inventory.capacity import used_capacity, free_capacity
from config.resources import RESOURCES


class CargoPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        cargo = []
        fuel_capacity = (
            self.game.player.spacecraft.definition.fuel_tank_capacity
        )
        for resource, amount in self.game.player.resources.items():
            if resource == "fuel":
                cargo_fuel = max(0, amount - fuel_capacity)
                if cargo_fuel > 0:
                    cargo.append(
                        f"FUEL: {cargo_fuel}"
                    )
            else:
                if amount > 0:
                    cargo.append(f"{resource.upper()}:{amount}")
        if cargo:
            cargo_spacecraft_text = " | ".join(cargo)
        else:
            cargo_spacecraft_text = "[dim]NO CARGO[/dim]"

        player = self.game.player
        text = (
            f"[bold cyan]CARGO:[/bold cyan] "
            f"{used_capacity(player, RESOURCES)}/"
            f"{self.game.player.spacecraft.definition.cargo_capacity} "
            f"[bold cyan]FREE:[/bold cyan] "
            f"{free_capacity(player, RESOURCES)}\n"
            f"{cargo_spacecraft_text}\n\n\n"
            )
        title_inside = "SHIP CARGO"
        return Panel(
            text,
            title=f"[bold cyan]{title_inside}[/bold cyan]",
            border_style="cyan"
        )
