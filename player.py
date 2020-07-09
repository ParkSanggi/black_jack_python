from abc import ABCMeta, abstractmethod

from score import Score

from input_view import InputView
from output_view import OutputView


class Gamer(metaclass=ABCMeta):

    def __init__(self):
        self.cards = list()

    def add_card(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

    def get_score(self):
        return Score(self.cards)

    def has_over_score(self):
        return Score(self.cards).is_over_black_jack()

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def need_more_cards(self):
        pass

    @abstractmethod
    def notice_addition(self):
        pass


class Player(Gamer):

    def __init__(self, name, betting_money):
        super().__init__()
        self.name = name
        self.betting_money = betting_money

    def get_name(self):
        return self.name

    def need_more_cards(self):
        response = ""

        while response != 'y' and response != 'n':
            response = InputView.input_need_more_card(self.name)
        if response == 'y':
            return True
        return False

    def notice_addition(self):
        OutputView.output_gamers_cards(self)
        OutputView.output_new_line()

    def get_betting_money(self):
        return self.betting_money


class Dealer(Gamer):

    def get_name(self):
        return "딜러"

    def need_more_cards(self):
        score = Score(self.cards)
        return not score.is_over_dealer_limit()

    def notice_addition(self):
        OutputView.output_notice_dealer_addition()
