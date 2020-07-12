from abc import ABCMeta, abstractmethod

from profit.score import Score

from view.input_view import InputView
from view.output_view import OutputView


class Gamer(metaclass=ABCMeta):

    def __init__(self):
        self.__cards = list()

    def add_card(self, card):
        self.__cards.append(card)

    def get_cards(self):
        return self.__cards

    def get_score(self):
        return Score(self.__cards)

    def has_over_score(self):
        return Score(self.__cards).is_over_black_jack()

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
        self.__name = name
        self.__betting_money = betting_money

    def get_name(self):
        return self.__name

    def need_more_cards(self):
        response = ""

        while response != 'y' and response != 'n':
            response = InputView.input_need_more_card(self.__name)
        if response == 'y':
            return True
        return False

    def notice_addition(self):
        OutputView.output_gamers_cards(self)
        OutputView.output_new_line()

    def get_betting_money(self):
        return self.__betting_money


class Dealer(Gamer):

    def get_name(self):
        return "딜러"

    def need_more_cards(self):
        score = Score(self.__cards)
        return not score.is_over_dealer_limit()

    def notice_addition(self):
        OutputView.output_notice_dealer_addition()
