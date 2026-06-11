from dataclasses import dataclass


@dataclass(slots=True)
class MarketItem:
    resource_key: str
    stock: int
    price: int
