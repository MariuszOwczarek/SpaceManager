from models.planet import PlanetDefinition

PLANETS = {
    "Mars": PlanetDefinition(
        name="Mars",
        shortcut="MAR",
        planet_type="Industrial Colony",
        color="cyan",
        cheap_resource="iron",
        resource_bonus="iron",
        native_resources=["iron", "fuel", "coal"],
        imported_resources={"silicone": 0.25,
                            "silver": 0.15}
    ),

    "Venus": PlanetDefinition(
        name="Venus",
        shortcut="VEN",
        planet_type="Trade Hub",
        color="green",
        cheap_resource="fuel",
        resource_bonus="fuel",
        native_resources=["fuel", "silver", "silicon"],
        imported_resources={"gold": 0.20,
                            "iron": 0.35,
                            "water": 0.40}
    ),

    "Jupiter": PlanetDefinition(
        name="Jupiter",
        shortcut="JUP",
        planet_type="Mining World",
        color="blue",
        cheap_resource="uranium",
        resource_bonus="uranium",
        native_resources=["uranium", "iron", "coal"],
        imported_resources={"fuel": 0.40,
                            "gold": 0.10,
                            "silicon": 0.15}
    ),

    "Saturn": PlanetDefinition(
        name="Saturn",
        shortcut="SAT",
        planet_type="Luxury Sector",
        color="yellow",
        cheap_resource="gold",
        resource_bonus="gold",
        native_resources=["gold", "silver", "fuel"],
        imported_resources={"uranium": 0.25,
                            "water": 0.30,
                            "iron": 0.20}
    ),

    "Mercury": PlanetDefinition(
        name="Mercury",
        shortcut="MER",
        planet_type="Scientific Outpost",
        color="magenta",
        cheap_resource="silicon",
        resource_bonus="silicon",
        native_resources=["silicon", "uranium", "gold"],
        imported_resources={"fuel": 0.5,
                            "silver": 0.20,
                            "gold": 0.10}
    ),
}
