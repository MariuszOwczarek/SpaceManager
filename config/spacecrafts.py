from models.spacecraft import SpacecraftDefinition


SPACECRAFTS = {
    "shuttle": SpacecraftDefinition(
        name="Titan Hauler",
        type="Shuttle",
        cargo_capacity=10000,
        fuel_tank_capacity=120,
        fuel_usage=2,
        speed=3,
        scanner_range=1,
    ),

    "freighter": SpacecraftDefinition(
        name="Orion VX-12",
        type="Freighter",
        cargo_capacity=250,
        fuel_tank_capacity=500,
        fuel_usage=5,
        speed=2,
        scanner_range=2,
    ),

    "industrial": SpacecraftDefinition(
        name="Nabuhodonozor",
        type="Industrial",
        cargo_capacity=500,
        fuel_tank_capacity=1000,
        fuel_usage=12,
        speed=1,
        scanner_range=2,
    ),
}
