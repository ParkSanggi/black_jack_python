
class Referee:

    def __init__(self, books):
        self.__books = books

    def judgement(self, dealer, player):
        dealer_score = dealer.get_score()
        player_score = player.get_score()
        betting_money = player.get_betting_money()
        dealer_name = dealer.get_name()
        player_name = player.get_name()

        if player_score.is_over_black_jack():
            self.__books.fill_in(dealer_name, player_name, betting_money)
        elif player_score.is_black_jack():
            if not dealer_score.is_black_jack():
                self.__books.fill_in(player_name, dealer_name, betting_money * 1.5)
        elif player_score.is_higher(dealer_score):
            self.__books.fill_in(player_name, dealer_name, betting_money)
        elif dealer_score.is_higher(player_score):
            if dealer_score.is_over_black_jack():
                return self.__books.fill_in(player_name, dealer_name, betting_money)
            elif dealer_score.is_black_jack():
                return self.__books.fill_in(dealer_name, player_name, betting_money * 1.5)
            self.__books.fill_in(dealer_name, player_name, betting_money)
