display_message = """
H A N G M A N
"""

print(display_message)

winning_word = "python"

# Prompt user for input
print("Guess the word: ")
guess = input()

# Check if  user guessed correctly
if guess == winning_word:
    print("You survived!")
else:
    print("You are hanged!)
