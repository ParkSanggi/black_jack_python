from gamer.gamers import Gamers
from card.deck import Deck


class BlackJackGame:

    def __init__(self):
        self.__deck = Deck()
        self.__gamers = Gamers()

    def start(self):
        self.__gamers.get_cards_for_starting(self.__deck)
        self.__gamers.show_cards()
        # Todo
        # 처음 두장이 블랙잭인 경우 배팅액의 1.5배로 변경 필요
        # 현재는 마지막에 모두 확인
        self.__gamers.get_additional_cards(self.__deck)
        self.__gamers.show_result()
        self.__gamers.show_final_profit()


if __name__ == '__main__':
    game = BlackJackGame()
    game.start()


