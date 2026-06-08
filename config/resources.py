from models.resource import Resource

RESOURCES = {
    "fuel": Resource(
        name="fuel",
        base_price=40,
        weight=0.5,
        category=""
    ),

    "coal": Resource(
        name="coal",
        base_price=60,
        weight=1.5,
        category=""
    ),

    "iron": Resource(
        name="iron",
        base_price=120,
        weight=2.0,
        category=""
    ),

    "gold": Resource(
        name="gold",
        base_price=250,
        weight=0.8,
        category=""
    ),

    "silicon": Resource(
        name="silicon",
        base_price=180,
        weight=1.2,
        category=""
    ),

    "uranium": Resource(
        name="uranium",
        base_price=450,
        weight=3.0,
        category=""
    ),

    "silver": Resource(
        name="silver",
        base_price=290,
        weight=1.0,
        category=""
    )
}
