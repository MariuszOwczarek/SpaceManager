from textual.containers import Horizontal
from ui.layouts.base_layout import BaseLayout
from textual.containers import Container
from ui.panels.status_panel import StatusPanel
from ui.panels.market_panel import MarketPanel
from ui.panels.facilities_panel import FacilitiesPanel


class HomeworldLayout(BaseLayout):
    def compose(self):
        with Horizontal(id="main_content"):
            yield Container(
                id="workspace_content"
            )

    def refresh_all(self):
        refreshables = [
            self.query_one(StatusPanel),
            self.query_one(MarketPanel),
            self.query_one(FacilitiesPanel)]

        for widget in refreshables:
            widget.refresh()
