from random import randint

from card.card_factory import CardFactory
from view.output_view import OutputView


class Deck:

    def __init__(self):
        self.__cards = CardFactory.create()
        self.__used = [False for _ in range(len(self.__cards))]

    def distribute_cards_for_starting(self, dealer, players):
        starting_cards_count = 2
        for _ in range(starting_cards_count):
            for player in players:
                player.add_card(self.__draw_card())
            dealer.add_card(self.__draw_card())
        OutputView.output_card_setting_for_starting_is_complete(players)

    def distribute_cards_sufficiently(self, dealer, players):
        for player in players:
            self.__give_cards_sufficiently(player)
        self.__give_cards_sufficiently(dealer)

    def __give_cards_sufficiently(self, gamer):
        while not gamer.has_over_score() and gamer.need_more_cards():
            gamer.add_card(self.__draw_card())
            gamer.acknowledge_receipt_of_card()

    def __draw_card(self):
        if self.__is_used_all_cards():
            self.__used = [False for _ in range(len(self.__cards))]
        card_count = len(self.__cards)
        idx = -1
        while self.__used[idx] or idx < 0:
            idx = randint(0, card_count - 1)
        self.__used[idx] = True
        return self.__cards[idx]

    def __is_used_all_cards(self):
        for i in range(len(self.__cards)):
            if not self.__used[i]:
                return False
        return True
