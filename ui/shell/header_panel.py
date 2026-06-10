from textual.widgets import Static
from rich.panel import Panel


class HeaderPanel(Static):
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
            fuel = self.game.player.resources["fuel"]
            fuel_capacity = (self.game.player.spacecraft
                             .definition.fuel_tank_capacity)
        text = (
            f"[bold cyan]TURN:[/bold cyan] "
            f"{self.game.turn}\n"
            f"[bold cyan]CREDITS:[/bold cyan] "
            f"{self.game.player.credits}\n"
            f"[bold cyan]SPACECRAFT TYPE:[/bold cyan] "
            f"{self.game.player.spacecraft.definition.type}\n"
            f"[bold cyan]SPACECRAFT NAME:[/bold cyan] "
            f"{self.game.player.spacecraft.definition.name}\n"
            f"[bold cyan]FUEL TANK:[/bold cyan] "
            f"{min(fuel, fuel_capacity)}/"
            f"{fuel_capacity}\n"
        )
        player = self.game.player
        title_inside = f"STAR MANAGER - {player.player_name.upper()}"
        return Panel(
            text,
            title=f"[bold cyan]{title_inside}[/bold cyan]",
            border_style="cyan"
        )
