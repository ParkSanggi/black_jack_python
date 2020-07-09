from symbol import Symbol


class Score:

    __BLACK_JACK = 21
    __DEALER_LIMIT = 16

    def __init__(self, cards):
        self.__score = 0
        __has_ace = False

        for card in cards:
            symbol = card.get_symbol()
            self.__score += symbol.value
            if symbol == Symbol.ACE:
                __has_ace = True
        if __has_ace and self.__score + 10 <= self.__BLACK_JACK:
            self.__score += 10

    def is_black_jack(self):
        return self.__score == self.__BLACK_JACK

    def is_over_black_jack(self):
        return self.__score > self.__BLACK_JACK

    def is_over_dealer_limit(self):
        return self.__score > self.__DEALER_LIMIT

    def is_higher(self, target_score):
        return self.__score > target_score.get_score()

    def get_score(self):
        return self.__score
