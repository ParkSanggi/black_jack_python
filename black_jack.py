from card.deck import Deck
from gamer.gamer import Dealer
from gamer.player_factory import PlayerFactory
from profit.books import Books
from view.output_view import OutputView


class BlackJackGame:

    def __init__(self):
        self.__deck = Deck()
        self.__dealer = Dealer()
        self.__players = PlayerFactory.create()
        self.__books = Books(self.__dealer.get_name(), self.__get_player_names())

    def start(self):
        self.__deck.distribute_cards_for_starting(self.__dealer, self.__players)
        self.__show_cards()
        self.__deck.distribute_cards_sufficiently(self.__dealer, self.__players)
        self.__show_final_score()
        self.__books.show_final_profit(self.__dealer, self.__players)

    def __show_cards(self):
        OutputView.output_cards_which_gamer_is_holding(self.__dealer)
        OutputView.output_new_line()
        for player in self.__players:
            OutputView.output_cards_which_gamer_is_holding(player)
            OutputView.output_new_line()

    def __show_final_score(self):
        OutputView.output_cards_which_gamer_is_holding(self.__dealer)
        OutputView.output_final_score(self.__dealer.get_score())
        for player in self.__players:
            OutputView.output_cards_which_gamer_is_holding(player)
            OutputView.output_final_score(player.get_score())

    def __get_player_names(self):
        names = list()
        for player in self.__players:
            names.append(player.get_name())
        return names


if __name__ == '__main__':
    game = BlackJackGame()
    game.start()


