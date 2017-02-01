import re
import os


class UI:
    @staticmethod
    def input_nick():
        nick = input("Enter your nickname: ")
        while not UI.is_valid_nickname(nick):
            nick = input("Enter your nickname (min. 3 chars): ")
        return nick

    @staticmethod
    def is_valid_nickname(nick):
        return bool(re.match("\w{3,}$", nick))

    @classmethod
    def select_player_from_list(cls):
        cls.print_player_table()
        return cls.input_select_player_kind()

    @classmethod
    def print_player_table(cls):
        pass

    @staticmethod
    def print_select_player_kinds():
        select_player_kinds = ['New player', 'Player from players list']
        UI.print_universal_number_list(select_player_kinds)

    @classmethod
    def input_select_player_kind(cls):
        player_kind = cls.universal_number_input(2)
        if player_kind == "1":
            return "new"
        if player_kind == "2":
            return "from list"

    @classmethod
    def universal_number_input(cls, max_input_number):
        number_input = input("Enter number: ").strip()
        while not cls.is_valid_input_number(number_input, max_input_number):
            number_input = input("Enter number between 1 and {}: ".format(max_input_number))
        return number_input

    @staticmethod
    def is_valid_input_number(number_input, max_input_number):
        return number_input.isnumeric() and int(number_input) <= max_input_number

    @staticmethod
    def print_try_kinds():
        try_kinds = ['Enter letter', 'Enter all word']
        UI.print_universal_number_list(try_kinds)

    @staticmethod
    def print_universal_number_list(list_to_print):
        for index, text in enumerate(list_to_print):
            print('({}) {}'.format(index+1, text))

    @classmethod
    def input_try_kind(cls):
        try_kind = cls.universal_number_input(2)
        if try_kind == "1":
            return "letter"
        if try_kind == "2":
            return "word"

    @classmethod
    def input_letter(cls):
        letter = input('Enter letter: ').strip()
        while not cls.is_valid_letter(letter):
            letter = input('Enter letter: ').strip()
        return letter.upper()

    @staticmethod
    def is_valid_letter(letter):
        return bool(re.match(r'^[A-Za-z]$', letter))

    @classmethod
    def input_all_word(cls):
        word = input('Enter word: ').strip()
        while not cls.is_valid_word(word):
            word = input('Enter word (only letters and spaces): ').strip()
        return word.upper()

    @staticmethod
    def is_valid_word(word):
        return bool(re.match(r'[A-Za-z ]+$', word))

    @staticmethod
    def print_lives(lives):
        print("You have {} live{}".format(lives, 's' if lives > 1 else ''))

    @staticmethod
    def print_dashes(dashes):
        print(' '.join(list(dashes)))

    @staticmethod
    def screen_clear():
        os.system('clear')

    @staticmethod
    def print_used_letters(used_letters):
        print('Used letter: {}'.format(', '.join(sorted(list(set(used_letters))))))

    @staticmethod
    def print_attempts_counts(attempts):
        print('Attempt no. {}.'.format(attempts))


    @classmethod
    def input_is_continue(cls):
        to_is_continue = cls.universal_number_input(2)
        if to_is_continue == "1":
            return "yes"
        if to_is_continue == "2":
            return "no"
    @staticmethod
    def print_to_continue_question():
        print("Next game?")
        to_continue_answers = ['Yes', 'No']
        UI.print_universal_number_list(to_continue_answers)

    @staticmethod
    def print_win_information(correct_word):
        print("You won!")
        print("{} was word to guess".format(correct_word))

    @staticmethod
    def print_fail_information(correct_word):
        print("You failed!")
        print("{} was word to guess".format(correct_word))