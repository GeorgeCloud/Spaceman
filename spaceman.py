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
    dash = "-" * 32

    # refractor
    guesses_left = 7

    print("Welcome to Spaceman!")
    print("The secret word contains 5 letters")
    print("You have 7 incorect guesses, please enter only one letter")
    print(dash)

    while True:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha():
            guess = input("Enter a letter: ").lower()
            continue
        try:
            print(correct_word)
            index = word_left.index(guess)
            # print(f"index: {index}")
            print("Your guess appears in the word!")
            hidden_word[index] = guess
            word_left[index] = "-"
            # CHECK FOR DUPLICATE LETTERS, # of occurences
            print(f"Guesses word so far: {''.join(hidden_word)}")
        except:
            guesses_left -= 1
            print("Sorry your guess was not in the word, try again")
            print(f"Your have {guesses_left} guesses left")

        if correct_word == "".join(hidden_word):
            print(f"Nice you guessed the word: {correct_word} with {guesses_left} attempts left!")
            break
            # if True in [True for c in word_left if c.isdigit()]

        elif guesses_left < 1:
            print("You Lost..............")
            break

start_spaceman()
