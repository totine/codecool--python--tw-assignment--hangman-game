class Player:
    players = []

    def __init__(self, nick):
        self.nick = nick
        self.results = []
        Player.players.append(self)

    def set_nick(self, nick):
        self.nick = nick

    @classmethod
    def add_new_player(cls, nick):
        return Player(nick)

    @classmethod
    def get_player(cls, nick):
        for player in cls.players:
            if player.get_nick() == nick:
                return player

    @classmethod
    def select_player_from_list(cls, index):
        return cls.players[index]

    @classmethod
    def get_players_list(cls):
        return cls.players

    @classmethod
    def get_players_nicks_list(cls):
        return [player.nick for player in cls.players]

    def get_nick(self):
        return self.nick

    def add_result(self, result):
        self.results.append(result)

