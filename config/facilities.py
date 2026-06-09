from models.facilities import Facility

FACILITIES = {
    "hospital": Facility(
        name="hospital",
        credits=2500,
        resources={
            "iron": 100,
            "fuel": 50,
        },
        population=20,
        effects={
            "health": 7,
            "happiness": 3
        }
    ),

    "school": Facility(
        name="school",
        credits=3000,
        resources={
            "iron": 80,
            "silicon": 50,
        },
        population=15,
        effects={
            "happiness": 6
        }
    ),

    "factory": Facility(
        name="factory",
        credits=3500,
        resources={
            "fuel": 100,
            "uranium": 75,
        },
        population=30,
        effects={
            "population": 5,
            "happiness": -2
        }
    ),

    "barracks": Facility(
        name="barracks",
        credits=3500,
        resources={
            "silver": 80,
            "fuel": 100,
        },
        population=25,
        effects={
            "safety": 8,
            "happiness": -5
        }
    ),

    "housing": Facility(
        name="housing",
        credits=2200,
        resources={
            "silver": 60,
            "fuel": 20,
        },
        population=10,
        effects={
            "max_population": 500,
            "happiness": 2
        }
    ),

    "farms": Facility(
        name="farms",
        credits=2200,
        resources={
            "water": 100,
            "fuel": 20,
        },
        population=0,
        effects={
            "population": 2,
        }
    ),

    "reactor": Facility(
        name="reactor",
        credits=5000,
        resources={
            "uranium": 150,
            "iron": 100,
        },
        population=0,
        effects={
            "industry": 2,
            "happiness": -2
        }
    ),

    "warehouse": Facility(
        name="warehouse",
        credits=7000,
        resources={
            "uranium": 150,
            "iron": 100,
            "fuel": 50
        },
        population=0,
        effects={
            "storage_capacity": 500
        }
    ),
}
