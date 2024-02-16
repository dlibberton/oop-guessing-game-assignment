# init with integer
# GuessingGame#guess
#

import random

class GuessingGame:
    def __init__(self, answer):
        self.answer = answer
        self.last_guess = None
        self.last_result = None

    def solved(self):
        return self.last_result == "correct"

    def guess(self, number):
        number = int(number)
        if number == self.answer:
            self.last_result = "correct"
        elif number < self.answer:
            self.last_result = "too low"
        else:
            self.last_result = "too high"
        self.last_guess = number
        return self.last_result

# ----- main.py -----from readme
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
    if last_guess != None: 
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")

    last_guess  = input("Enter your guess: ")
    last_result = game.guess(last_guess)

print(f"{last_guess} was correct!")
