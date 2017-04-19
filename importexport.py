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

    @classmethod
    def export_players(cls, filepath):
        with open(filepath, 'w') as player_csv:
            fieldnames = ['nick']
            player_writer = csv.DictWriter(player_csv, fieldnames)
            player_writer.writeheader()
            player_list = Player.get_players_list()
            for player in player_list:
                player_dict = {'nick': player.get_nick()}
                player_writer.writerow(player_dict)

    @classmethod
    def export_results(cls, filepath):
        with open(filepath, 'w') as results_csv:
            fieldnames = ['player_nick', 'word_to_guess', 'lives', 'attempts']
            results_writer = csv.DictWriter(results_csv, fieldnames)
            results_writer.writeheader()
            results_list = HangmanResult.get_results()
            for result in results_list:
                player_nick = result.get_player().get_nick()
                results_dict = {'player_nick': player_nick, 'word_to_guess': result.get_word_to_guess(),
                                'lives': result.get_saved_lives(), 'attempts': result.get_attempts()}
                results_writer.writerow(results_dict)

    @classmethod
    def all_exports(cls, player_file_path='Data/players.csv', results_file_path='Data/results.csv'):
        cls.export_players(player_file_path)
        cls.export_results(results_file_path)
