from ui.layouts.base_layout import BaseLayout
from textual.containers import Container


class ForeignLayout(BaseLayout):
    def compose(self):
        yield Container(
            id="workspace_content"
        )
