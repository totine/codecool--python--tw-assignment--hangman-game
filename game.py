from hangman import Hangman, HangmanResult
from player import Player
from ui import UI
from importexport import CsvImport



class Game:
    game_results = []
    is_continue = True
    is_game_intro = True
    game_options = ['Start game', 'Help', 'Score table', 'Credits', 'Exit']

    def __init__(self, player, hangman):
        self.player = player
        self.hangman = hangman
        self.game_result = None



    @classmethod
    def get_game_options(cls):
        return cls.game_options

    @classmethod
    def get_is_game_intro(cls):
        return cls.is_game_intro

    @classmethod
    def get_is_continue(cls):
        return cls.is_continue

    @classmethod
    def game_intro(cls):
        UI.start_screen()
        option = UI.input_game_options()
        if option == "1":
            cls.start_game_prepare()
        if option == "2":
            cls.show_help()
        if option == "3":
            cls.show_score_table()
        if option == "4":
            cls.show_credits()
        if option == "5":
            cls.exit_game()

    @classmethod
    def start_game_prepare(cls):
        cls.is_game_intro = False

    @classmethod
    def show_help(cls):
        UI.print_help()

    @classmethod
    def show_score_table(cls):
        pass

    @classmethod
    def show_credits(cls):
        UI.print_credits()

    @classmethod
    def exit_game(cls):
        UI.print_goodbye()
        cls.is_game_intro = False
        cls.is_continue = False

    @classmethod
    def start_game(cls):
        player = cls.select_player()
        hangman = Hangman()
        return Game(player, hangman)

    @classmethod
    def select_player(cls):
        player_kind = cls.choice_player_select_kind()
        if player_kind == "new":
            nick = cls.get_new_player_nick()
            return Player.add_new_player(nick)
        elif player_kind == "from list":
            cls.get_player_from_list()

    @classmethod
    def choice_player_select_kind(cls):
        UI.print_select_player_kinds()
        return UI.input_select_player_kind()

    @classmethod
    def get_new_player_nick(cls):
        nick = UI.input_nick()
        while nick in Player.get_players_nicks_list():
            UI.print_nick_is_taken()
            nick = UI.input_nick()
        return nick

    @classmethod
    def get_player_from_list(cls):
        player_list = Player.get_players_nicks_list()
        index = UI.select_player_from_list(player_list)
        return Player.select_player_from_list(int(index) - 1)

    def game_screen(self):
        UI.screen_clear()
        UI.print_attempts_counts(self.hangman.get_attempts_counts())
        UI.print_used_letters(self.hangman.get_used_letters())
        UI.print_lives(self.hangman.get_lives())
        UI.print_dashes(self.hangman.get_dashes())

    def game_body(self):
        while self.hangman.get_dashes() != self.hangman.get_word_to_guess() and self.hangman.get_lives() > 0:
            self.game_screen()
            self.hangman.next_try()
        if self.hangman.get_dashes() == self.hangman.get_word_to_guess():
            UI.print_win_information(self.hangman.get_word_to_guess())
        if self.hangman.get_lives() == 0:
            UI.print_fail_information(self.hangman.get_word_to_guess())

    def game_end(self):
        self.save_results()
        UI.print_to_continue_question()
        to_is_continue = UI.input_is_continue()
        if to_is_continue == "no":
            UI.print_goodbye()
            Game.is_continue = False

    def save_results(self):
        HangmanResult.add_result(self.hangman.get_word_to_guess(), self.hangman.get_lives(),
                                 self.hangman.get_attempts_counts(), self.player)


def main():
    CsvImport.all_imports()
    while Game.get_is_game_intro():
        Game.game_intro()
    while Game.get_is_continue():
        game = Game.start_game()
        game.game_body()
        game.game_end()
    CsvImport.all_exports()


main()
