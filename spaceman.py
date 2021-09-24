from random import choice

YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

def get_word_list():
    with open("words.txt") as file:
        words = file.readlines()[0].rstrip().split(' ')
        file.close()
        return words


def start_spaceman():
    words = get_word_list()
    correct_word = choice(words)
    word_left = list(correct_word)
    correct_word_len = len(correct_word)
    hidden_word = list("_" * correct_word_len)
    letters_not_guessed = list("abcdefghijklmnopqrstuvwxyz")
    dash = "-" * 100
    guesses_left = 7

    print("Welcome to Spaceman!")
    print("The secret word contains 5 letters")
    print("You have 7 incorect guesses, please enter only one letter")
    print(dash)

    while True:
        guess = input("Enter a letter: ").lower()
        if not guess.isalpha() or guess not in letters_not_guessed:
            print("Only letters allowed! Can't guess same letter")
            continue

        print(f"correct word: {correct_word}")

        letters_not_guessed.remove(guess)
        occurences = word_left.count(guess)

        if occurences:
            for _ in range(occurences):
                index = word_left.index(guess)
                hidden_word[index] = guess
                word_left[index] = "-"
                print("Your guess appears in the word!")
                print(f"Guessed word so far: {''.join(hidden_word)}")
                print(f"Letters not guessed yet: {', '.join(letters_not_guessed)}")
                print(dash)
        else:
            guesses_left -= 1
            print("Sorry your guess was not in the word, try again")
            print(f"Your have {guesses_left} guesses left")
            continue

        if correct_word == "".join(hidden_word):
            print(f"Nice you guessed the word: {correct_word} with {guesses_left} attempts left!")
            break

        elif guesses_left < 1:
            print("You Lost..............")
            break

start_spaceman()
