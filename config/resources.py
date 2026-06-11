from models.resource import ResourceDefinition

RESOURCES = {
    "fuel": ResourceDefinition(
        name="fuel",
        base_price=40,
        weight=0.5,
        category=""
    ),

    "coal": ResourceDefinition(
        name="coal",
        base_price=60,
        weight=1.5,
        category=""
    ),

    "iron": ResourceDefinition(
        name="iron",
        base_price=120,
        weight=2.0,
        category=""
    ),

    "gold": ResourceDefinition(
        name="gold",
        base_price=250,
        weight=0.8,
        category=""
    ),

    "silicon": ResourceDefinition(
        name="silicon",
        base_price=180,
        weight=1.2,
        category=""
    ),

    "uranium": ResourceDefinition(
        name="uranium",
        base_price=450,
        weight=3.0,
        category=""
    ),

    "silver": ResourceDefinition(
        name="silver",
        base_price=290,
        weight=1.0,
        category=""
    ),

    "water": ResourceDefinition(
        name="water",
        base_price=100,
        weight=1.0,
        category=""
    )
}
