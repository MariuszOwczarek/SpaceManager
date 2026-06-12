from utils.ui import add_log
from app.refresh import refresh_all
from systems.turns.pipeline import run_turn_pipeline


def handle_turn_end(game, app):
    game.turn += 1
    run_turn_pipeline(game)
    add_log(game,
            f"TURN {game.turn}")

    refresh_all(app)
