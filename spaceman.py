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
    word_left = correct_word
    correct_word_len = len(correct_word)
    hidden_word = "_" * correct_word_len
    dash = "-" * 32

    # refractor
    guesses_left = 7

    print("Welcome to Spaceman!")
    print("The secret word contains 5 letters")
    print("You have 7 incorect guesses, please enter only one letter")
    print(dash)

    # Check if only letter isalpha
    guess = input("Enter a letter: ").lower()

    while True
        if guess.isalpha():
            guess = input("Enter a letter: ")
            # return back; continue
        try:
            index = word_left.index(guess)
            if index:
                hidden_word[index] = guess
            # if guess in word_left:
            #     word_left
        # except ValueError as e:
        #     raise e



        guesses_left -= 1
        if guess_attempt == correct_word or guesses_left < 1:
            break


    import pdb; pdb.set_trace()


start_spaceman()
