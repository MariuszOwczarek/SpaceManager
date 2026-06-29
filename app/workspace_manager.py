from ui.panels.planet_panel import PlanetPanel


async def load_workspace(app):
    container = app.current_layout.query_one("#workspace_content")

    await container.remove_children()
    workspace_name = app.current_workspace

    workspace = None
    if workspace_name == "overview":
        planet = app.game.planets[app.game.current_planet]
        if planet.definition.is_homeworld:
            workspace = PlanetPanel(app.game)

    if workspace is not None:
        await container.mount(workspace)
