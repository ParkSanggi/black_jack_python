from gamer.names import PlayerNames
from gamer.gamer import Player
from profit.betting_money import BettingMoney


class PlayerFactory:

    @staticmethod
    def create():
        player_names = PlayerNames()
        player_name = player_names.get_next_name()
        players = list()

        while player_name:
            players.append(Player(player_name, BettingMoney()))
            player_name = player_names.get_next_name()
        return players
