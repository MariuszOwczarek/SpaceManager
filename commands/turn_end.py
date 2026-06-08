from systems.production import factory_production
from systems.population import hospital_population
from systems.economy import resource_price_change, resource_quantity_change


def handle_turn_end(game, app):
    game.turn += 1
    for planet_name, planet in game.planets.items():
        resource_price_change(planet)
        resource_quantity_change(planet)
        factory_production(planet, planet_name, game)
        hospital_population(planet, planet_name, game)
    game.save_market_data(game.current_planet)
    game.add_log("TURN ENDED")
    app.refresh_all()
