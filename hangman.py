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

# Prompt user for input
guess = input("Guess the word: ")

# Check if  user guessed correctly
if guess == winning_word:
    print("You survived!")
else:
    print("You are hanged!")