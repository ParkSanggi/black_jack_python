
class InputView:

    @classmethod
    def input_betting_money(cls):
        return input("베팅할 금액을 입력해주세요.")

    @classmethod
    def input_player_names(cls):
        return input("게임에 참여할 플레이어들의 이름을 입력해주세요. ','로 구분")

    @classmethod
    def input_need_more_card(cls, name):
        return input("{}는 한장의 카드를 더 받겠습니까?".format(name))
