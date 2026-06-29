from textual.widget import Widget


class BaseLayout(Widget):
    def __init__(self, game, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = game

    def refresh_all(self):
        pass
