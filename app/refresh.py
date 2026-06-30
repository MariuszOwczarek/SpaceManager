from ui.shell.logs_panel import LogsPanel
from ui.shell.header_panel import HeaderPanel
from ui.shell.cargo_panel import CargoPanel
from ui.shell.warehouse_panel import WarehousePanel
from ui.shell.intel_panel import IntelPanel
from ui.shell.command_panel import CommandsPanel


def refresh_shell(app):
    app.query_one(HeaderPanel).refresh()
    app.query_one(CargoPanel).refresh()
    app.query_one(CommandsPanel).refresh()
    app.query_one(WarehousePanel).refresh()
    app.query_one(LogsPanel).refresh()
    app.query_one(IntelPanel).refresh()


def refresh_layout(app):
    layout = app.current_layout
    if layout is not None:
        layout.refresh_all()


def refresh_all(app):
    refresh_shell(app)
