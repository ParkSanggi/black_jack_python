
class OutputView:

    @classmethod
    def output_new_line(cls):
        print('')

    @classmethod
    def output_card_setting_for_starting_is_complete(cls, players):
        name_count = len(players)

        print("딜러와 ", end='')
        for i in range(name_count):
            print(players[i].get_name(), end='')
            if i != name_count - 1:
                print(", ", end='')
            else:
                print("에게 2장의 카드를 나누었습니다.")

    @classmethod
    def output_cards_which_gamer_is_holding(cls, gamer):
        cards = gamer.get_cards()
        card_count = len(cards)
        name = gamer.get_name()

        print("{} : ".format(name), end='')
        for i in range(card_count):
            print("{} {}".format(cards[i].get_symbol().value, cards[i].get_type().name), end='')
            if i != card_count - 1:
                print(", ", end='')

    @classmethod
    def output_dealer_has_received_card(cls):
        print("딜러는 16이하라 한장의 카드를 받았습니다.")

    @classmethod
    def output_final_score(cls, score):
        print(" - 결과: {}".format(score.get_score()))

    @classmethod
    def output_final_profit(cls, books):
        print("## 최종 수익")
        for transaction in books:
            print("{}: {}".format(transaction[0], transaction[1]))


