from systems.population.population import hospital_population


def population_system(game):
    for planet_name, planet in game.planets.items():
        hospital_population(planet, planet_name, game)
