from models.buildings import Buildings

BUILDINGS = {
    "hospital": Buildings(
        name="hospital",
        credits=2000,
        resources={
            "iron": 10,
            "fuel": 5,
        },
        population=20,
    ),

    "school": Buildings(
        name="school",
        credits=1800,
        resources={
            "iron": 8,
            "silicon": 5,
        },
        population=15,
    ),

    "factory": Buildings(
        name="factory",
        credits=3500,
        resources={
            "iron": 20,
            "fuel": 15,
            "uranium": 2,
        },
        population=30,
    ),

    "barracks": Buildings(
        name="barracks",
        credits=2500,
        resources={
            "iron": 15,
            "fuel": 10,
        },
        population=25,
    ),
}
