from ui.layouts.foreign_layout import ForeignLayout
from ui.layouts.homeworld_layout import HomeworldLayout


async def load_layout(app):
    container = app.query_one("#main_content")

    await container.remove_children()

    planet = app.game.planets[app.game.current_planet]

    if planet.definition.is_homeworld:
        layout = HomeworldLayout(app.game)
    else:
        layout = ForeignLayout(app.game)

    await container.mount(layout)

    app.current_layout = layout
