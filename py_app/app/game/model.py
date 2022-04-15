
from dataclasses import dataclass, field
from enum import Enum, auto
from pyclbr import Function
import random

class Action(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def __str__(self):
        return self.name

WIN_LIST = {
    (Action.PAPER, Action.ROCK): "covers",
    (Action.ROCK, Action.SCISSORS): "crushes",
    (Action.SCISSORS, Action.PAPER): "cuts"
}

class PlayerType(Enum):
    HUMAN = auto()
    CPU = auto()
    NONE = auto()

@dataclass(frozen=True)
class Player:
    name: str
    player_type: PlayerType

    def __repr__(self):
        return self.name

@dataclass
class Model:
    score: int = 0
    players: list = field(default_factory=dict)
    actions: dict = field(default_factory=dict)
    player_idx: int = 0

    def start(self) -> None:
        self.score = 0
        self.players = {}

    def add_player(self, player: Player) -> int:
        self.player_idx += 1
        self.players[self.player_idx] = player
        return self.player_idx

    def get_player(self, idx: int) -> Player:
        return self.players[idx] 

    def get_players(self) -> dict:
        return self.players

    def add_action(self, player_idx: int, action: Action) -> None:
        self.actions[player_idx] = action

    def get_actions(self) -> dict:
        return self.actions

    def clear_actions(self) -> None:
        self.actions = {}