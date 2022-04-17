from dataclasses import dataclass
from joe_first_test_app.game.model import Model, Action, Player
from typing import Tuple


from abc import ABC, abstractmethod

@dataclass
class View(ABC):
    model: Model

    def display_actions(self) -> None:
        actions = self.model.get_actions()
        for k, v in actions.items():
            self.display_action(player=k, action=v)

    def get_int(self, value: str) -> Tuple[bool, int]:
        success = True
        out_val = 0
        try:
            out_val = int(value)
        except ValueError:
            success = False
        return (success, out_val)

    def start(self) -> None:
        self.display_state()

    def get_action(self, player_idx: int) -> Action:
        action_dict =  {a[0]:a[1] for a in enumerate(Action)}
        selection = self.get_menu_item(action_dict)
        return selection

    @abstractmethod
    def display_action(self, player: Player, action: Action) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_menu_item(self, in_items: dict):
        raise NotImplementedError

    @abstractmethod
    def display_state(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def display_result(self, winner: Player, action_set: tuple, result: str) -> None:
        raise NotImplementedError
