

class Referee:

    def __init__(self, books):
        self.books = books

    def judgement(self, dealer, player):
        dealer_score = dealer.get_score()
        player_score = player.get_score()
        betting_money = player.get_betting_money()
        dealer_name = dealer.get_name()
        player_name = player.get_name()

        if player_score.is_over_black_jack():
            self.books.fill_in((dealer_name, player_name, betting_money))
        elif player_score.is_black_jack():
            if not dealer_score.is_black_jack():
                self.books.fill_in(player_name, dealer_name, betting_money * 1.5)
        elif player_score.is_higher(dealer_score):
            self.books.fill_in(player_name, dealer_name, betting_money)
        elif dealer_score.is_higher(player_score):
            if dealer_score.is_over_black_jack():
                self.books.fill_in(player_name, dealer_name, betting_money)
            elif dealer_score.is_black_jack():
                self.books.fill_in(dealer_name, player_name, betting_money * 1.5)
            self.books.fill_in(dealer_name, player_name, betting_money)

#
# """
# 딜러와 플레이어들의 점수를 계산한다
#
#  플레이어가 먼저 21을 넘으면 진다
#
#     플레이어가 블랙잭인지 확인한다.
#         플레이어가 블랙잭인 경우
#             딜러가 블랙잭이면 비긴다.
#             딜러가 블랙잭이 아니면 이긴다. 플레이어 : +배팅액 * 1.5, 딜러 : -배팅액 * 1.5
#         플레이어가 블랙잭이 아닌 경우.
#             딜러가 블랙잭이면 패배한다. 플레이어 : -배팅액, 딜러 : +배팅액
#             딜러의 스코어와 비교한다
#                 딜러보다 높으면 이긴다. 플레이어 : +배팅액, 딜러 : -배팅액
#                 딜러와 같으면 비긴다.
#                 """

