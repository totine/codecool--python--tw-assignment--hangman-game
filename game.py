from hangman import Hangman, HangmanResult
from player import Player
from ui import UI



class Game:
    game_results = []
    is_continue = True

    def __init__(self, player, hangman):
        self.player = player
        self.hangman = hangman
        self.game_result = None


    @classmethod
    def start_game(cls):
        player = cls.select_player()
        hangman = Hangman()
        return Game(player, hangman)

    @classmethod
    def select_player(cls):
        player_kind = cls.choice_player_select_kind()
        if player_kind == "new":
            nick = UI.input_nick()
            return Player.add_new_player(nick)

        if player_kind == "from list":
            index = UI.select_player_from_list()
            return Player.select_player_from_list(index)

    @classmethod
    def choice_player_select_kind(cls):
        UI.print_select_player_kinds()
        return UI.input_select_player_kind()

    def game_body(self):

        while self.hangman.get_dashes() != self.hangman.get_word_to_guess() and self.hangman.get_lives() > 0:
            self.game_screen()
            self.hangman.next_try()

        if self.hangman.get_dashes() == self.hangman.get_word_to_guess():
            self.hangman.hangman_end_success()
        if self.hangman.get_lives() == 0:
            self.hangman.hangman_end_fail()

    def game_screen(self):
        UI.screen_clear()
        UI.print_attempts_counts(self.hangman.get_attempts_count())
        UI.print_used_letters(self.hangman.get_used_letters())
        UI.print_lives(self.hangman.get_lives())
        UI.print_dashes(self.hangman.get_dashes())

    def game_end(self):
        UI.print_to_continue_question()
        to_is_continue = UI.input_is_continue()
        if to_is_continue == "no":
            Game.is_continue = False

    @classmethod
    def get_is_continue(cls):
        return cls.is_continue






def main():
    while Game.get_is_continue():
        game = Game.start_game()
        game.game_body()
        game.game_end()


main()
