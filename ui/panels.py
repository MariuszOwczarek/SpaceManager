from textual.containers import Horizontal, Vertical
from textual.widgets import Static
from rich.panel import Panel
from rich.table import Table
from config.resources import RESOURCES
from config.planets import PLANETS
from config.buildings import BUILDINGS
from config.player import PLAYER_DATA


class HeaderPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        cargo = []
        fuel_capacity = (
            self.game.player["spacecraft_fuel_capacity"]
        )
        for resource, amount in self.game.player["resources"].items():
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
                cargo_text = " | ".join(cargo)
            else:
                cargo_text = "[dim]NO CARGO[/dim]"
            fuel = self.game.player["resources"]["fuel"]
            fuel_capacity = self.game.player["spacecraft_fuel_capacity"]
            text = (
                f"[bold cyan]TURN:[/bold cyan] "
                f"{self.game.turn}\n"
                f"[bold cyan]CREDITS:[/bold cyan] "
                f"{self.game.player['credits']}\n"
                f"[bold cyan]SPACECRAFT TYPE:[/bold cyan] "
                f"{self.game.player['spacecraft_type']}\n"
                f"[bold cyan]SPACECRAFT NAME:[/bold cyan] "
                f"{self.game.player['spacecraft_name']}\n"
                f"[bold cyan]CARGO:[/bold cyan] "
                f"{self.game.used_capacity()}/"
                f"{self.game.player['spacecraft_capacity']}\n"
                f"[bold cyan]FREE:[/bold cyan] "
                f"{self.game.free_capacity()}\n\n"
                f"[bold cyan]FUEL TANK:[/bold cyan] "
                f"{min(fuel, fuel_capacity)}/"
                f"{fuel_capacity}\n"
                f"{cargo_text}"
            )
        player = PLAYER_DATA["player"]
        title_inside = f"STAR MANAGER - {player.player_name.upper()}"
        return Panel(
            text,
            title=f"[bold cyan]{title_inside}[/bold cyan]",
            border_style="cyan"
        )


class LogsPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        if self.game.logs:
            logs = "\n".join(f"> {log}" for log in self.game.logs)
        else:
            logs = "[dim]NO LOGS[/dim]"
        return Panel(logs,
                     title="[green]ACTION LOGS[/green]",
                     border_style="green")


class StatusPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        planet = self.game.planets[self.game.current_planet]
        table = Table(expand=True)
        table.add_column("ATTRIBUTE")
        table.add_column("VALUE")
        table.add_row("Max Population", str(planet["max_population"]))
        table.add_row("Population", str(planet["population"]))
        table.add_row("Health", str(planet["health"]))
        table.add_row("Happiness", str(planet["happiness"]))
        table.add_row("Safety", str(planet["safety"]))
        planet_color = (PLANETS[self.game.current_planet].color)

        return Panel(table,
                     title=f"[{planet_color}]"
                     f"CURRENT STATUS"
                     f"[/{planet_color}]",
                     border_style=planet_color)


class MarketPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        planet = self.game.planets[self.game.current_planet]
        table = Table(expand=True)
        table.add_column("RESOURCES")
        table.add_column("AVAIL")
        table.add_column("PRICE")
        table.add_column("WGHT")

        for resource_key, resource in RESOURCES.items():
            market_item = (planet["market"][resource_key])
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
        planet_color = (PLANETS[self.game.current_planet].color)
        return Panel(table,
                     title=f"[{planet_color}]"
                     f"MARKET PLACE"
                     f"[/{planet_color}]",
                     border_style=planet_color)


class BuildingsPanel(Static):
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
        for building_key in BUILDINGS:
            requirements = (
                BUILDINGS[building_key]
            )
            resource_text = ", ".join(
                f"{res}:{amt}"
                for res, amt in (
                    requirements.resources.items()
                )
            )
            table.add_row(
                building_key.upper(),
                str(planet["buildings"][building_key]),
                str(requirements.credits),
                resource_text
            )
        planet_color = (PLANETS[self.game.current_planet].color)
        return Panel(table,
                     title=f"[{planet_color}]"
                     f"FACILITY PROGRESS"
                     f"[/{planet_color}]",
                     border_style=planet_color)


class PlanetPanel(Vertical):

    def __init__(self, game, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.game = game

    def compose(self):
        with Horizontal(classes="planet_content"):
            yield StatusPanel(
                self.game,
                id="status"
            )

            yield MarketPanel(
                self.game,
                id="market"
            )

            yield BuildingsPanel(
                self.game,
                id="buildings"
            )

    def refresh_planet_style(self):
        planet_name = (
            self.game.current_planet
        )

        planet_type = (
            PLANETS[planet_name].planet_type
        )

        planet_color = (
            PLANETS[planet_name].color
        )

        self.border_title = (
            f"[{planet_color}]"
            f"PLANET "
            f"{planet_name.upper()} "
            f"COMMAND CENTER "
            f"[/]"
            f"([dim]"
            f"{planet_type.upper()}"
            f"[/dim])"
        )

        self.styles.border = (
            "solid",
            planet_color
        )

        self.refresh()


class IntelPanel(Static):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def render(self):
        table = Table(expand=True)
        table.add_column("RESOURCES")
        for planet_name in self.game.market_memory.keys():
            short_name = PLANETS[planet_name].shortcut
            age = self.game.turn - self.game.market_memory[planet_name]["turn"]
            table.add_column(f"{short_name} {age}T")

        for resource in RESOURCES:
            row = [resource.upper()]
            for planet_name in self.game.market_memory.keys():
                price = (self.game
                         .market_memory[planet_name]["prices"][resource])

                row.append(str(price))
            table.add_row(*row)
        return Panel(
            table,
            title="[magenta]MARKET INTEL[/magenta]",
            border_style="magenta"
        )


class CommandsPanel(Static):
    def render(self):
        help_text = """
        [bold cyan]COMMANDS[/bold cyan]
        move | buy | sell | build | end | exit
        """
        return Panel(
            help_text,
            title="[bold blue]COMMAND HELP[/bold blue]",
            border_style="blue"
        )
