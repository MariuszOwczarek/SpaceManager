from ui.panels.planet_panel import PlanetPanel


async def load_workspace(app):
    container = app.current_layout.query_one("#workspace_content")

    await container.remove_children()

    workspace = None
    if app.current_workspace == "overview":
        print("Mounting PlanetPanel")
        workspace = PlanetPanel(app.game)

    if workspace is not None:
        print("Mounting PlanetPanel")
        await container.mount(workspace)
