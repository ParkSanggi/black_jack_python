from view.input_view import InputView


class PlayerNames:

    def __init__(self):
        temp_names = []
        while not self.__is_valid(temp_names):
            temp_names = InputView.input_player_names().split(',')
        self.__names = iter(temp_names)

    @staticmethod
    def __is_valid(temp_names):
        if not temp_names:
            return False
        for name in temp_names:
            if len(name) > 10 or len(name) < 1:
                return False
        return True

    def get_next_name(self):
        try:
            return self.__names.__next__()
        except StopIteration:
            return ""
