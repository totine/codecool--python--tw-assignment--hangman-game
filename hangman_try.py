import random
import sys

LIST_OF_CAPITALS = ['AMSTERDAM', 'ANDORRA LA VELLA', 'ATHENS', 'BELGRADE',
        'BERLIN', 'BERN', 'BRATISLAVA', 'BRUSSELS', 'BUCHAREST', 'BUDAPEST',
        'CHISINAU', 'COPENHAGEN', 'DUBLIN', 'HELSINKI', 'KIEV', 'LISBON', 'LJUBLJANA',
        'LONDON', 'LUXEMBOURG', 'MADRID', 'MINSK', 'MONACO', 'MOSCOW', 'NICOSIA',
        'NUUK', 'OSLO', 'PARIS', 'PODGORICA', 'PRAGUE', 'REYKJAVIK', 'RIGA', 'ROME',
        'SAN MARINO', 'SARAJEVO', 'SKOPJE', 'SOFIA', 'STOCKHOLM', 'TALLINN', 'TIRANA',
        'VADUZ', 'VALLETTA', 'VATICAN CITY', 'VIENNA', 'VILNIUS', 'WARSAW', 'ZAGREB']
word_to_guess = random.choice(LIST_OF_CAPITALS)
word_from_letters = []
lives = 5
word_to_guess_letters_list = []
all_answer = ""

print(word_to_guess)


for i in range (len(word_to_guess)):
    word_to_guess_letters_list.append(word_to_guess[i])


for i in range(len(word_to_guess)):
    if word_to_guess[i] == " ":
        word_from_letters.append(' ')
    else:
        word_from_letters.append(' _ ')
print(word_from_letters)
for i in range (len(word_to_guess)):
    print(word_from_letters[i], end="")

print("\n")

while word_to_guess_letters_list != word_from_letters and all_answer != word_to_guess and lives > 0:
    next_step = input("Do you want to input letter [1] or input all answer [2]: ")
    if next_step == "1":
        input_letter = input("Input letter: ")
        while 1:
            if input_letter.isalpha():
                if input_letter == "exit":
                    sys.exit("Looser!")
                else:
                    input_letter=input_letter.strip()
                    if len(input_letter)>1:
                            input_letter = input("Input only one letter: ")
                    else:
                        input_letter = input_letter.upper()
                        break
            else:
                input_letter = input("Input letter: ")
        print(input_letter)

        how_many_letters_in_word = word_to_guess.count(input_letter)
        print(how_many_letters_in_word)

        input_letter_all_positions=[]
        searching_start=0
        for i in range (how_many_letters_in_word):
                input_letter_position=word_to_guess.find(input_letter,searching_start)
                input_letter_all_positions.append(input_letter_position)
                searching_start=input_letter_position+1
        if how_many_letters_in_word == 0:
            lives = lives-1

        print(lives)

        for i in input_letter_all_positions:
            word_from_letters[i] = input_letter

        for i in range (len(word_from_letters)):
            print(word_from_letters[i], end="")

    elif next_step == "2":
        all_answer = input("Wprowadź odpowiedź")
        all_answer = all_answer.strip()
        while 2:

            if all_answer.isalpha():
                if all_answer == "exit":
                    sys.exit("Looser!")
                all_answer = all_answer.upper()
                if all_answer == word_to_guess:
                    print("It's correct answer!")
                else:
                    print("It wasn't correct answer")
                break
            else:
                print("It wasn't correct answer")
                break

        break

    #elif next_step == "exit":
        #sys.exit("Looser!")
    #else:
    #    next_step = input("Do you want to input letter [1] or input all answer[2]: ")

if lives == 0 or all_answer != word_to_guess:
    print("Game over")
else:
    print("You win")
