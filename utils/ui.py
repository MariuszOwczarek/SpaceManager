def fail(game, app, message):
    game.add_log(message)
    app.refresh_all()
    return
