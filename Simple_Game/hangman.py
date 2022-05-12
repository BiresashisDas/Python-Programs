# Author :- Biresashis Das

# How to create a Hangman Game.

  """   Hangman is a game where you have to guess a letter to complete the random word that computer will generate. 
        If u successfully guessed all the letters than u will win the game. 
        For every wrong guessed u will lose a life. You have only seven chances. 
        If you guessed the letter wrong for 7 times you will eventually lost the game   """
  

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
words = ["frog", "apple", "dictionary", "mango"]  #You can add many words as you want in the list. The more words you will enter the more interesting the game will be.

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
    
    
    
    
    
    
