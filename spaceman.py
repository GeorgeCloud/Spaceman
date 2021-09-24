from random import choice
from os import system

YELLOW, RED, ENDC = '\033[93m', '\033[91m', '\033[0m'

def get_word_list():
    with open("words.txt") as file:
        words = file.readlines()[0].rstrip().split(' ')
        file.close()
        return words

def start_spaceman():
    system('clear')
    dash = "-" * 110
    words = get_word_list()
    correct_word = choice(words)
    word_left = list(correct_word)
    correct_word_len = len(correct_word)
    hidden_word = list("_" * correct_word_len)
    letters_not_guessed = list("abcdefghijklmnopqrstuvwxyz")
    guesses_left = correct_word_len

    print(f"""
          Welcome to Spaceman!
          The secret word contains {correct_word_len} letters
          You have {guesses_left} incorect guesses, please enter only one letter
          """)

    while True:
        print(f"""{dash}
        Your have {guesses_left} guesses left
        {YELLOW}Letters not guessed yet: {', '.join(letters_not_guessed) + ENDC}
        Guessed word so far: {''.join(hidden_word)}
        """)

        guess = input("Enter a letter: ").lower()
        system('clear')
        if not guess.isalpha() or guess not in letters_not_guessed:
            print(f"{RED}Only only letter is allowed! Can't guess same letter{ENDC}")
            continue

        letters_not_guessed.remove(guess)
        occurences = word_left.count(guess)

        if occurences:
            for _ in range(occurences):
                index = word_left.index(guess)
                hidden_word[index] = guess
                word_left[index] = "-"
                print("Your guess appears in the word!")
        else:
            guesses_left -= 1
            print(f"{RED}Sorry your guess was not in the word, try again{ENDC}")

            if guesses_left == 0:
                print(f"{RED}You Lost................{ENDC}")
                print(f"The correct word was: {YELLOW + correct_word + ENDC}")
                break
            continue

        if correct_word == "".join(hidden_word):
            print(f"Nice you guessed the word: {correct_word} with {guesses_left} attempts left!")
            break

start_spaceman()
