from random import randint

from card_factory import CardFactory


class Deck:

    def __init__(self):
        self.__cards = CardFactory.create()
        self.used = [False for _ in range(len(self.__cards))]

    def draw_card(self):
        if self.__is_empty():
            self.__cards.extend(CardFactory.create())
        card_count = len(self.__cards)
        idx = -1
        while self.used[idx] or idx < 0:
            idx = randint(0, card_count - 1)
        self.used[idx] = True
        return self.__cards[idx]

    def __is_empty(self):
        for i in range(len(self.__cards)):
            if not self.used[i]:
                return False
        return True
