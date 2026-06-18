from ui.layouts.base_layout import BaseLayout
from textual.containers import Container


class ForeignLayout(BaseLayout):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def compose(self):
        yield Container(
            id="workspace_content"
        )

    def refresh_all(self):
        refreshables = [

        ]
        for widget_type in refreshables:
            widgets = self.query(
                widget_type
            )

            if widgets:
                widgets.first().refresh()
