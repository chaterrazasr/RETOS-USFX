import random
import time

with open("wordlist.txt", 'r') as f:
        lines = f.readlines()
        wordlist = [line.strip() for line in lines]
with open("flag.txt", 'r') as f:
        flag = f.readline()

print(wordlist)
word = random.choice(wordlist)
guesses = []
rounds = 1

while True:
   print("debug mode: ", word)
   if(rounds > 1):
      if(time.time() > start_the_clock):
         print("Time is up!")
         quit()
   print("Round ", rounds)
   guess = input("Guess a five-letter word: ")
   if len(guess) != 5:
      print("Please enter a five-letter word.")
      continue
   if (guess == word):
      print("Congratulations! You guessed the word:", word)
      rounds = rounds + 1
      word = random.choice(wordlist)
      guesses = []
      if(rounds == 2):
         print("Start the clock, you have 10 seconds to win 4 more games!")
         start_the_clock = time.time()+10   
      if(rounds == 6):
         print("You have won the game:", flag)
         quit()
   else:
      guesses.append(guess)
      feedback = ""
      for i in range(5):
         if guess[i] == word[i]:
            feedback += guess[i]
         elif guess[i] in word:
            feedback += "-"
         else:
            feedback += "*"
      print("Feedback:", feedback)
      print("Previous guesses:", guesses)

