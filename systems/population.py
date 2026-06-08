def hospital_population(planet, planet_name, game):
    hospitals = (
        planet.buildings["hospital"])

    if hospitals > 0:
        if planet.population < planet.max_population:
            growth = int(
                hospitals * (planet.health/50)
                )
            planet.population += growth
            if (
                planet.population > planet.max_population
            ):
                planet.population = (
                    planet.max_population
                )
            game.add_log(
                f"{planet_name}: "
                f"POPULATION +{growth}"
            )
