# Importing random module for pseudo-random functionality
import random

display_message = """
H A N G M A N
"""
print(display_message)

# List of random words to choose from
word_list = ["python", "java", "kotlin", "javascript"]

# Seeding the random behavior
# No argument passed, seeding from current system time
random.seed()

# Shuffle sequence around then choose random word from list
random.shuffle(word_list)
winning_word = random.choice(word_list)

# Give player a hint by
# obscuring the word using hyphens
# length of hint is equal to length of winning word minus first 3 letters
hint = "-"*(len(winning_word) - 3)

# Prompt user for input
# Showing the first 3 letters of the word as hing
guess = input("Guess the word " + winning_word[:3] + hint + ": > ")

# Check if  user guessed correctly
if guess == winning_word:
    print("You survived!")
else:
    print("You lost!")
