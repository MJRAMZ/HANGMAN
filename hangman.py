# Importing random module for pseudo-random functionality
import random

title_display = """===================
H A N G M A N
====================
"""
print(title_display)

# List of random words to choose from
word_list = ["python", "java", "kotlin", "javascript"]

# Total number of tries use has in order to win
TRIES = 10

# String format for displaying current tries
tries_left = "You have {} attempts left."

# Seeding the random behavior
# No argument passed, seeding from current system time
random.seed()

# Shuffle sequence around then choose random word from list
random.shuffle(word_list)
winning_word = random.choice(word_list)

# Give player a hint by
# obscuring the word using hyphens
# length of hint is equal to length of winning word minus first 3 letters
wordlength = len(winning_word)
hint = "-"*(wordlength)
guess_index = []

# keep the game alive as long as the user still
# has tries left
while TRIES > 0:

    # Display total number of attempts left
    print(tries_left.format(str(TRIES)))

    print(hint)
    # Prompt user for input
    # Showing the first 3 letters of the word as hing
    guess = input("Guess the word: > ")
   # Check if  user guessed a letter correctly
    if guess in winning_word:
        TRIES -= 1
        guess_index = [index for index, element in enumerate(list(winning_word)) if element in guess]
        for j in guess_index:
            hint = hint[:j] + guess + hint[j + 1:]
        if hint == winning_word:
            print("\nThe word was: " + hint)
            print("Congratulations! You won")
            print("""Thanks for playing!\nWe'll see how well you did in the next stage""")
            quit(0)
    else:
        TRIES -= 1
        print("That letter doesn't appear in the word\n")

print("The word was: " + hint)
print("Sorry, you lost")
print("Better luck next time")
