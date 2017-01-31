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
    def select_player_from_list(cls, index):
        return cls.players[index]

