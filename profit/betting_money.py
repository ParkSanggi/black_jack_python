from view.input_view import InputView


class BettingMoney:

    def __init__(self):
        user_input = ""

        while not self.is_valid(user_input):
            user_input = InputView.input_betting_money()
        self.money = float(user_input)

    def __mul__(self, other):
        self.money *= other
        return self

    def __add__(self, other):
        self.money += other
        return self

    def __sub__(self, other):
        self.money -= other
        return self

    @staticmethod
    def is_valid(user_input):
        if not user_input.isdigit() or float(user_input) < 0:
            return False
        return True

    def get_money(self):
        return self.money
