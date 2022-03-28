'''
Lotto - Simulation
Erzeuge sechs eindeutige Zufallszahlen im Bereich 1-45 und speichere sie in einer Liste.
Erlaube dem User ebenfalls sechs eindeutige Zahlen im Bereich 1-45 einzugeben.

Vergleiche die User-Zahlen mit den zufälligen Lotto-Zahlen und teile dem User
mit wie viele seiner Zahlen mit den zufälligen Lotto-Zahlen übereinstimmen.
31.01.22
Phillip
'''
import random
import time

print("------------------------------------------------")
print("|                 Lotto Game                   |")
print("|               Phillip Hilscher               |")
print("------------------------------------------------")
print("")


print("Welcome player")
print("Maybe you got some luck today and win something ;)")

#empty lists and variables for counting, user inputs and the lotto numbers themselfs
lotto_numbers = []
user_input = []
number_count = 1
right_guesses = []
x = 1

#random numbers getting generated
while (len(lotto_numbers) < 6 ):
    zz = random.randint(1,45)
    if (zz not in lotto_numbers):
        lotto_numbers.append(zz)


#the user inputing numbers
while (number_count < 7 ):
    input_var = (int(input("Please state your {} number : ".format(number_count))))
    
    if (input_var not in user_input)and(input_var > 0)and(input_var<46):
        user_input.append(input_var)
        number_count = number_count + 1
    else:
        print("Your number was invalid, beacuse it's alredy added to your list, was too low or high.\nYour numbers have to be between 0 and 47")

#empty lines for spacing
print()
print()

#calculating wich numbers were correct
for x in range (0,6,1):
    if (user_input[x] in lotto_numbers):
        right_guesses.append(user_input[x])


#printing and countig of right guesses
number_rg =len(right_guesses)
if (number_rg < 6):
    print("You had {} numbers correct".format(number_rg))
    print("Your correct numbers were \n{}".format(right_guesses))

#if all guesses were correct
else:
    print("Congratulations, You won. (●__●)")
    print("You had all numbers correct.")
    print("")
    print("Your winnig numbers were, \n {}".format(right_guesses))


time.sleep(60)