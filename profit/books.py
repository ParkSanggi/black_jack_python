from profit.referee import Referee
from view.output_view import OutputView


class Books:

    def __init__(self, dealer_name, player_names):
        self.__books = dict()
        self.__books[dealer_name] = 0
        for name in player_names:
            self.__books[name] = 0

    def show_final_profit(self, dealer, players):
        for player in players:
            Referee.judgement(dealer, player, self)
        OutputView.output_final_profit(self.__get_contents())

    def fill_in(self, winner_name, loser_name, betting_money):
        self.__books[winner_name] += betting_money.get_money()
        self.__books[loser_name] -= betting_money.get_money()

    def __get_contents(self):
        return self.__books.items()
