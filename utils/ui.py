from app.refresh import refresh_all


def add_log(game, message):
    game.logs.append(message)

    if len(game.logs) > 8:
        game.logs.pop(0)


def fail(game, app, message):
    add_log(game, message)
    refresh_all(app)
    return
