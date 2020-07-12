from random import randint

from card.card_factory import CardFactory


class Deck:

    def __init__(self):
        self.__cards = CardFactory.create()
        self.__used = [False for _ in range(len(self.__cards))]

    def draw_card(self):
        if self.__is_used_all():
            self.__used = [False for _ in range(len(self.__cards))]
        card_count = len(self.__cards)
        idx = -1
        while self.__used[idx] or idx < 0:
            idx = randint(0, card_count - 1)
        self.__used[idx] = True
        return self.__cards[idx]

    def __is_used_all(self):
        for i in range(len(self.__cards)):
            if not self.__used[i]:
                return False
        return True
