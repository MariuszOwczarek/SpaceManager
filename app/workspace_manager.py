async def load_workspace(app):
    container = app.query_one("#workspace_content")

    await container.remove_children()
    workspace_name = app.current_workspace

    if workspace_name == "overwiew":
        planet = app.game.planet[app.game.current_planet]
        if planet.definition.is_homeworld:
            workspace = GlobalOverwiewWorkspace()
        else:
            workspace = LocalOverwiewWorkspace()

    if workspace_name == "warehouse":
        planet = app.game.planet[app.game.current_planet]
        if planet.definition.is_homeworld:
            workspace = GlobalWarehouseWorkspace()
        else:
            workspace = LocalWarehouseWorkspace()

    await container.mount(workspace)
