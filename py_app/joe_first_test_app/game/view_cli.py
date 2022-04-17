from joe_first_test_app.game.view import View
from joe_first_test_app.game.model import Action, Player

class ViewCLI(View):
    def display_action(self, player: Player, action: Action) -> None:
        print(f"{player}: {action.name}")

    def get_menu_item(self, in_items: dict):
        success = False
        selection = None
        while(not success or (selection is None)):
            print("\n".join([f"{k}) {v}" for (k, v) in in_items.items()]))
            value = input("Select an option:\n")
            success, int_val = self.get_int(value)
            selection = in_items.get(int_val,None)
        return selection

    def display_state(self) -> None:
        print(f"{self.model.score=}")
        print(f"{self.model.players=}")
        
    def display_result(self, winner: Player, action_set: tuple, result: str) -> None:
        print(f"{winner} : {action_set[0]} {result} {action_set[1]}")