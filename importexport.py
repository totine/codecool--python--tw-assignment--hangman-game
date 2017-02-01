import csv
from hangman import Hangman, HangmanResult
from player import Player

class CsvImport:
    @classmethod
    def import_words(cls, filepath):
        with open(filepath) as source:
            words_to_import = csv.DictReader(source)
            for word in words_to_import:
                Hangman.add_word(word['word'].upper())
    @classmethod
    def import_players(cls, filepath):
        with open(filepath) as source:
            players_to_import = csv.DictReader(source)
            for player in players_to_import:
                Player.add_new_player(player['nick'])

    @classmethod
    def import_results(cls, filepath):
        with open(filepath) as source:
            results_to_import = csv.DictReader(source)
            for result in results_to_import:
                player = Player.get_player(result['player_nick'])
                HangmanResult.add_result(result['word_to_guess'], result['lives'], result['attempts'], player)

    @classmethod
    def all_imports(cls, words_file_path='Data/words.csv', player_file_path='Data/players.csv', results_file_path='Data/results.csv'):
        cls.import_words(words_file_path)
        cls.import_players(player_file_path)
        cls.import_results(results_file_path)
