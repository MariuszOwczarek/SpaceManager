from models.spacecrafts import Spacecrafts


SPACECRAFTS = {
    "shuttle": Spacecrafts(
        name="Titan Hauler",
        type="Shuttle",
        cargo_capacity=60,
        fuel_tank=120,
        fuel_usage=2,
        speed=3,
        scanner_range=1,
    ),

    "freighter": Spacecrafts(
        name="Orion VX-12",
        type="Freighter",
        cargo_capacity=250,
        fuel_tank=500,
        fuel_usage=5,
        speed=2,
        scanner_range=2,
    ),

    "industrial": Spacecrafts(
        name="Nabuhodonozor",
        type="Industrial",
        cargo_capacity=500,
        fuel_tank=1000,
        fuel_usage=12,
        speed=1,
        scanner_range=2,
    ),
}
