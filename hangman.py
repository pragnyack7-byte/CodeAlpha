import random 

words = ["python","biology","genome","protein","enzyme"]

secret_word = random.choice(words)

lives = 6

guessed_letters = []

print("Welcome to Hangman!")

while lives > 0:

    print("\nLives:",lives)

    guess = input("Guess a letter: ")

    if guess in guessed_letters:
      print("You already guessed that letter!")
      continue

    guessed_letters.append(guess)

    word_guessed = True

    for letter in secret_word:
       if letter in guessed_letters:
          print(letter,end=" ")
       else:
        print("_", end=" ")
        word_guessed = False

    if guess in secret_word:
     print("\nGood guess!")
    else:
     print("\nWrong guess!")
     lives = lives - 1

    if word_guessed:
      print("\nCongratulations! You Won!")
      break
if lives == 0:
  print("\nGame Over!")
  print("The secret word was:", secret_word)