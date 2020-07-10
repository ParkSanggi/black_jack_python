
class Card:

    def __init__(self, symbol, card_type):
        self.symbol = symbol
        self.type = card_type

    def get_type(self):
        return self.type

    def get_symbol(self):
        return self.symbol
