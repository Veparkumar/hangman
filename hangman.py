word_list = ["aardvak", "baboon" , "camel"]

import random
chosen_word = random.choice(word_list)

print(f"pssst, the solution is {chosen_word}.")

guess = input("Guess a letter:").lower()

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Worng")

display = []
word_length = len(chosen_word)
for letter in chosen_word:
  display += "_"
print(display)

end_of_game = False 

while end_of_game:
  guess = input("Guess a letter: ").lower()
  
  for position in range(word_lenght):
    letter = chosen_word[position]
    print(f"current position: {position}\n 
    current letter:{letter}\n Guessed letter: {guess}")
    if letter == guessed_letter:
      dislay[position] = letter
  
  print(display)

  if "_" not in display:
    end_of_games = True
    print("you win.")

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
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter:").lower()

  
  for position in range(word_lenght):
    letter = chosen_word[positon]

  if letter == guess:
    display[position] = letter

  else:
    print("No match")

  if letter == guess:
    display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("you losw.")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("you win.")

  print(stages[lives])
  