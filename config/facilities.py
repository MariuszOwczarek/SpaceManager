from models.facilities import FacilityDefinition

FACILITIES = {
    "hospital": FacilityDefinition(
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

    "school": FacilityDefinition(
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

    "factory": FacilityDefinition(
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

    "barracks": FacilityDefinition(
        name="barracks",
        credits=3500,
        resources={
            "silver": 80,
            "fuel": 100,
        },
        population=100,
        effects={
            "safety": 8,
            "happiness": -5,
            "soldiers": 80
        }
    ),

    "housing": FacilityDefinition(
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

    "farms": FacilityDefinition(
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

    "reactor": FacilityDefinition(
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

    "warehouse": FacilityDefinition(
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
