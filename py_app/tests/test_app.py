from app.game import game, controller, model, view_cli
import pytest


@pytest.mark.parametrize(
    "param1,param2",
    [
        (model.Action.PAPER, model.Action.ROCK),
        (model.Action.ROCK, model.Action.SCISSORS),
        (model.Action.SCISSORS, model.Action.PAPER),
    ]
)
class TestApp:
    @pytest.fixture
    def setup(self):
        self.model = model.Model()
        self.view = view_cli.ViewCLI(model = self.model)
        self.controller = controller.Controller(model = self.model, view = self.view)
        return self

    def test_actions(self, param1, param2, setup):
        p1 = setup.model.add_player(model.Player(name="aaa", player_type=model.PlayerType.HUMAN))
        p2 = setup.model.add_player(model.Player(name="bbb", player_type=model.PlayerType.CPU))
        setup.model.add_action(p1, param1)
        setup.model.add_action(p2, param2)
        winner, _, _ = setup.controller.evaluate()
        assert winner == p1
