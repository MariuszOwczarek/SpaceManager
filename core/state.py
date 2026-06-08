from config.economy import RESOURCES, RESOURCE_WEIGHT
from config.planets import PLANET_BONUSES
from config.buildings import BUILDINGS
import random

from config.spacecrafts import SPACECRAFTS
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
        self.player = {
            "credits": PLAYER_DATA["credits"],
            "spacecraft_type": SPACECRAFTS["industrial"]["type"],
            "spacecraft_name": SPACECRAFTS["industrial"]["name"],
            "spacecraft_capacity": SPACECRAFTS["shuttle"]["cargo_capacity"],
            "spacecraft_fuel_capacity": SPACECRAFTS["shuttle"]["fuel_tank"],
            "resources": {resource: 0 for resource in RESOURCES},
        }
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

        if len(self.logs) > 10:
            self.logs.pop(0)

    # =====================================================
    # GENERATORS
    # =====================================================
    def generate_prices(self):
        return {
            "fuel": random.randint(5, 20),
            "coal": random.randint(10, 30),
            "iron": random.randint(20, 50),
            "gold": random.randint(80, 200),
            "silicon": random.randint(40, 100),
            "uranium": random.randint(150, 400),
            "silver": random.randint(50, 120),
        }

    def generate_resources(self):
        return {resource: random.randint(20, 100) for resource in RESOURCES}

    def generate_building_costs(self):
        return {building: random.randint(1500, 3500) for building in BUILDINGS}

    # =====================================================
    # PLANETS
    # =====================================================
    def create_planet(self, name):
        prices = self.generate_prices()
        cheap_resource = PLANET_BONUSES[name]["cheap"]
        prices[cheap_resource] = int(prices[cheap_resource] * 0.7)
        return {
            "max_population": random.randrange(3000, 11_000, 1000),
            "resources": self.generate_resources(),
            "prices": prices,
            "buildings": {building: 0 for building in BUILDINGS},
            "population": random.randint(300, 1000),
            "health": random.randint(40, 80),
            "happiness": random.randint(40, 80),
            "safety": random.randint(50, 70)
        }

    # =====================================================
    # MARKET MEMORY
    # =====================================================
    def save_market_data(self, planet_name):
        self.market_memory[planet_name] = {
            "turn": self.turn,
            "prices": self.planets[planet_name]["prices"].copy(),
        }

    # =====================================================
    # CARGO
    # =====================================================
    def used_capacity(self):
        total = 0
        fuel_tank_capacity = (
            self.player["spacecraft_fuel_capacity"]
        )
        for resource, amount in self.player["resources"].items():
            if resource == "fuel":
                cargo_fuel = max(0, amount - fuel_tank_capacity)
                total += (cargo_fuel * RESOURCE_WEIGHT[resource])
            else:
                total += (amount * RESOURCE_WEIGHT[resource])
        return round(total, 1)

    def free_capacity(self):
        return round(self.player["spacecraft_capacity"] -
                     self.used_capacity(), 1)

    def fuel_used_capacity(self):
        fuel = self.player["resources"]["fuel"]
        return fuel

    def free_fuel(self):
        return round(self.player["spacecraft_fuel_capacity"] -
                     self.fuel_used_capacity(), 1)

    def cargo_fuel(self):
        total_fuel = self.player["resources"]["fuel"]
        fuel_capacity = self.player["spacecraft_fuel_capacity"]
        return max(0, total_fuel - fuel_capacity)
