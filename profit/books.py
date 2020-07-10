
class Books:

    def __init__(self, dealer_name, player_names):
        self.books = dict()
        self.books[dealer_name] = 0
        for name in player_names:
            self.books[name] = 0

    def fill_in(self, winner_name, loser_name, betting_money):
        self.books[winner_name] += betting_money.get_money()
        self.books[loser_name] -= betting_money.get_money()

    def get_contents(self):
        return self.books.items()
