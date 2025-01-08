import random
stages = [1,2,3,4,5,6]
lives = 6
#word_list = ["aardvark", "baboon", "camel"]
from word_bank import word_list
chosen_word = random.choice (word_list)
#print (chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range (word_length):
  placeholder += "_"
print("here is how many letters are in the word: " + placeholder)


game_over = False
correct_letter = []

while not game_over:
  guess = input ("Guess a letter: ").lower()

  if guess in correct_letter:
    print (f"you already chosen this letter {guess}")
  
#step_2 display
  display = ""

  for letter in chosen_word:
    if letter == guess:
       display += letter
       correct_letter.append(guess)
    elif letter in correct_letter:
      display += letter
    else:
       display += "_"

  print(display)

  #countin lives
  
  if guess not in chosen_word:
    lives -= 1
    print(f"You have {lives} lives left")
    if lives == 0:
      game_over = True
      print(f"***** It was {chosen_word}. You lose*****")

  if "_" not in display:
    print(f"***** It was {chosen_word}. You won!******")
    game_over = True
  

