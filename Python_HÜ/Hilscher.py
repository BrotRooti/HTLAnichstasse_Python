'''
kleines Zahlenreaten-Spiel mit fixer untergrenze 0
Spiler wird nach der obergrenze gefragt
Phillip H.
17.01.22
'''

import random
#user geeretings and ask for upper limit
ul = int(input("Hello, and welcome, to my small number guessing game. Please state an upper limit:"))

#calculate the secret random number
z = random.randint(0,ul)
#counter variable to count tries of the user
count = 1

#game loop starts
while(True):

    #in the gameloop compare user input with secret number
    ans = int(input("Please state your guess:"))

       #if it is correct congratulations message and break
    if (z == ans):
        print("Congratulation")
        print("Your Answer was correct")
        print("It took you {} tries to get here".format(count))
        break
        
        #if it is not correct, increase counter and give a hint (e.g. my number is greater ...)
    elif (z < ans):
       print("Your guess was incorrect.")
       print("This was your {} guess".format(count))
       print("Hint:")
       print("My number is smaller than your guess")
       count = count + 1
    elif (z > ans):
        print("Your guess was incorrect.")
        print("This was your {} guess".format(count))
        print("Hint:")
        print("My number is greater than your guess")
        count = count + 1