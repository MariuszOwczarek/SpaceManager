from textual.containers import Vertical
from textual.widgets import Static


class ForeignLayout(Vertical):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def compose(self):
        yield Static("FOREIGN TERMINAL")

    def refresh_all(self):
        refreshables = [

        ]
        for widget_type in refreshables:
            widgets = self.query(
                widget_type
            )

            if widgets:
                widgets.first().refresh()
