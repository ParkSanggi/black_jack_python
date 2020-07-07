
class Gamer:

    def __init__(self):
        self.cards = list()

    def add_card(self, card):
        self.cards.append(card)


class Player(Gamer):

    def __init__(self, name, betting_money):
        super().__init__()
        self.name = name
        self.betting_money = betting_money


class Dealer(Gamer):
    pass
