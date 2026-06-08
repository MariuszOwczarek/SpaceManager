from config.resources import RESOURCES
from config.planets import PLANETS
from config.buildings import BUILDINGS
import random
from models.market import MarketItem
from models.planet import PlanetState
from config.player import PLAYER_DATA


# =========================================================
# GAME STATE
# =========================================================
class GameState:
    def __init__(self):
        self.turn = 1
        self.current_planet = "Mars"
        self.logs = []
        self.market_memory = {}
        self.player = PLAYER_DATA["player"]
        self.planets = {
            "Mars": self.create_planet("Mars"),
            "Venus": self.create_planet("Venus"),
            "Jupiter": self.create_planet("Jupiter"),
            "Saturn": self.create_planet("Saturn"),
            "Mercury": self.create_planet("Mercury"),
        }
        self.add_log("WELCOME COMMANDER")
        self.save_market_data(self.current_planet)

    # =====================================================
    # LOGS
    # =====================================================
    def add_log(self, message):
        self.logs.append(message)

        if len(self.logs) > 8:
            self.logs.pop(0)

    # =====================================================
    # GENERATORS
    # =====================================================
    def create_market(self, planet_name):
        market = {}
        cheap_resource = (PLANETS[planet_name].cheap_resource
                          )
        for resource_key, resource in RESOURCES.items():
            base_price = resource.base_price

            if resource_key == cheap_resource:
                base_price = int(base_price*0.7)

            market[resource_key] = MarketItem(
                resource_key=resource_key,
                stock=random.randint(30, 120),
                price=random.randint(
                    int(base_price * 0.7),
                    int(base_price * 1.34)
                )
            )
        return market

    def generate_building_costs(self):
        return {building: random.randint(1500, 3500) for building in BUILDINGS}

    # =====================================================
    # PLANETS
    # =====================================================
    def create_planet(self, name):
        return PlanetState(
                definition=PLANETS[name],
                market=self.create_market(name),
                buildings={building: 0 for building in BUILDINGS},
                population=random.randint(300, 1000),
                max_population=random.randrange(3000, 11_000, 1000),
                health=random.randint(40, 80),
                happiness=random.randint(40, 80),
                safety=random.randint(50, 70)
            )

    # =====================================================
    # MARKET MEMORY
    # =====================================================
    def save_market_data(self, planet_name):
        market = self.planets[planet_name].market
        prices = {resource_key: market_item.price
                  for resource_key, market_item in market.items()
                  }

        self.market_memory[planet_name] = {
            "turn": self.turn,
            "prices": prices,
        }

    # =====================================================
    # CARGO
    # =====================================================
    def used_capacity(self):
        total = 0
        fuel_tank_capacity = (
            self.player.spacecraft.definition.fuel_tank_capacity
        )
        for resource_key, amount in self.player.resources.items():
            resource = RESOURCES[resource_key]
            if resource_key == "fuel":
                cargo_fuel = max(0, amount - fuel_tank_capacity)
                total += (cargo_fuel * resource.weight)
            else:
                total += (amount * resource.weight)
        return round(total, 1)

    def free_capacity(self):
        cargo_capacity = self.player.spacecraft.definition.cargo_capacity
        return round(cargo_capacity -
                     self.used_capacity(), 1)

    def fuel_used_capacity(self):
        fuel = self.player.resources["fuel"]
        return fuel

    def free_fuel(self):
        return round(self.player.spacecraft.definition.fuel_tank_capacity -
                     self.fuel_used_capacity(), 1)

    def cargo_fuel(self):
        total_fuel = self.player.resources["fuel"]
        fuel_capacity = self.player.spacecraft.definition.fuel_tank_capacity
        return max(0, total_fuel - fuel_capacity)
