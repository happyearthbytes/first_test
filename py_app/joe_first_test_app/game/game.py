from joe_first_test_app.game.model import Model
from joe_first_test_app.game.view_cli import ViewCLI
from joe_first_test_app.game.controller import Controller

class game:
    def __init__(self) -> None:
        self.model = Model()
        self.view = ViewCLI(model = self.model)
        self.controller = Controller(model = self.model, view = self.view)

    def start(self) -> None:
        self.controller.start()