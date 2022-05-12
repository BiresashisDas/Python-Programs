# Author :- Biresashis Das

# How to create a Hangman Game.
#

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
words = ["donkey", "apple", "dictionary", "mango"]

choosen_word = random.choice(words)
#print("The choosen word is : ", choosen_word)

lives = 6

display = []
for _ in range(len(choosen_word)):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choosen_word:
        print(f"You choose a letter {guess}, that is not in the word. You loose a life.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lost")

    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
