from symbol import Symbol
from card_type import CardType
from card import Card


class CardFactory:

    @staticmethod
    def create():
        cards = list()
        for symbol in Symbol.__members__.values():
            CardFactory.__create_by_type(cards, symbol)
        return cards

    @staticmethod
    def __create_by_type(cards, symbol):
        for card_type in CardType.__members__.values():
            cards.append(Card(symbol, card_type))



