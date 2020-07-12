from gamer.gamer import Dealer
from gamer.player_factory import PlayerFactory
from profit.books import Books
from profit.referee import Referee
from view.output_view import OutputView


class Gamers:

    def __init__(self):
        self.__dealer = Dealer()
        self.__players = PlayerFactory.create()

    def get_cards_for_starting(self, deck):
        starting_cards_count = 2

        for _ in range(starting_cards_count):
            for p in self.__players:
                p.add_card(deck.draw_card())
            self.__dealer.add_card(deck.draw_card())
        OutputView.output_set_cards_for_starting(self.__get_player_names())

    def show_cards(self):
        OutputView.output_gamers_cards(self.__dealer)
        OutputView.output_new_line()
        for player in self.__players:
            OutputView.output_gamers_cards(player)
            OutputView.output_new_line()

    def get_additional_cards(self, deck):
        for player in self.__players:
            self.__get_more_cards(player, deck)
        self.__get_more_cards(self.__dealer, deck)

    def show_result(self):
        OutputView.output_gamers_cards(self.__dealer)
        OutputView.output_final_score(self.__dealer.get_score())
        for player in self.__players:
            OutputView.output_gamers_cards(player)
            OutputView.output_final_score(player.get_score())

    def show_final_profit(self):
        books = Books(self.__dealer.get_name(), self.__get_player_names())
        referee = Referee(books)
        for player in self.__players:
            referee.judgement(self.__dealer, player)
        OutputView.output_final_profit(books.get_contents())

    def __get_player_names(self):
        names = list()
        for player in self.__players:
            names.append(player.get_name())
        return names

    @staticmethod
    def __get_more_cards(gamer, deck):
        while not gamer.has_over_score() and gamer.need_more_cards():
            gamer.add_card(deck.draw_card())
            gamer.notice_addition()
