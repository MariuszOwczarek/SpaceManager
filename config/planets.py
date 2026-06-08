from models.planet import PlanetDefinition

PLANETS = {
    "Mars": PlanetDefinition(
        name="Mars",
        shortcut="MAR",
        planet_type="Industrial Colony",
        color="cyan",
        cheap_resource="iron",
        resource_bonus="iron",
    ),

    "Venus": PlanetDefinition(
        name="Venus",
        shortcut="VEN",
        planet_type="Trade Hub",
        color="green",
        cheap_resource="fuel",
        resource_bonus="fuel",
    ),

    "Jupiter": PlanetDefinition(
        name="Jupiter",
        shortcut="JUP",
        planet_type="Mining World",
        color="blue",
        cheap_resource="uranium",
        resource_bonus="uranium",
    ),

    "Saturn": PlanetDefinition(
        name="Saturn",
        shortcut="SAT",
        planet_type="Luxury Sector",
        color="yellow",
        cheap_resource="gold",
        resource_bonus="gold",
    ),

    "Mercury": PlanetDefinition(
        name="Mercury",
        shortcut="MER",
        planet_type="Scientific Outpost",
        color="magenta",
        cheap_resource="silicon",
        resource_bonus="silicon",
    ),
}
