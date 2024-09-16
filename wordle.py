word = "fault"

# color for printing
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

def generate_hint(guess):
    color = default
    for i in range(5):
        if (guess[i]==word[i]):
            color = green
        elif guess[i] in word:
            color = yellow
        else:
            color = default
        hint = hint + color + guess[i] + default
    return hint

def game_loop():
    userGuess = ""
    for i in range(6):
        userGuess = input("give a guess: ")
        print(generate_hint(userGuess))
        if userGuess == word:
            print("congratulations")
            break
game_loop()

