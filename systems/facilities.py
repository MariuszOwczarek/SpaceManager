from config.facilities import FACILITIES
from models.planet import PlanetState


def get_building_credit_cost(facility_key: str, planet: PlanetState):
    facility = FACILITIES[facility_key]
    return facility.credits * planet.construction_modifier


def get_building_resource_cost(facility_key: str, planet: PlanetState):
    facility = FACILITIES[facility_key]
    return {resource: (amount * planet.construction_modifier)
            for resource, amount in (
                facility.resources.items()
                                     )
            }
