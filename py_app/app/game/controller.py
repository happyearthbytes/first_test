from dataclasses import dataclass
from app.game.model import Model, Action, Player, PlayerType, WIN_LIST
from app.game.view import View
import random

@dataclass
class Controller:
    model: Model
    view: View

    def __post_init__(self) -> None:
        self.ACTION_MAP = {
            PlayerType.HUMAN: self.human_action,
            PlayerType.CPU: self.cpu_action
        }

    def start(self) -> None:
        self.model.start()
        self.set_players()
        self.view.start()
        self.get_commands()

    def set_players(self) -> None:
        self.model.add_player(Player(name="alice", player_type=PlayerType.HUMAN))
        self.model.add_player(Player(name="bob", player_type=PlayerType.CPU))

    def get_commands(self) -> None:
        for _, player in self.model.get_players().items():
            action = self.ACTION_MAP.get(player.player_type)(player)
            self.model.add_action(player_idx=player, action=action)
        self.view.display_actions()
        winner, action_set, result = self.evaluate()
        self.view.display_result(winner, action_set, result)
    
    def human_action(self, player_idx: int) -> Action:
        return self.view.get_action(player_idx)

    def cpu_action(self, player_idx: int) -> Action:
        selection = random.choice([a for a in Action])
        return selection

    def evaluate(self) -> None:
        win_side = 0
        winner = None
        result = None
        actions = self.model.get_actions()
        action_set = tuple(actions.values())
        player_set = tuple(actions.keys())
        if action_set not in WIN_LIST:
            action_set = (action_set[1], action_set[0])
            win_side = 1
        if action_set[0] is action_set[1]:
            winner = Player(name="tie", player_type=PlayerType.NONE)
            result = "ties"
        else:
            winner = player_set[win_side]
            result = WIN_LIST[action_set]
        return winner, action_set, result