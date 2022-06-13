import random

b = 0
while b == 0:
    a = input("Enter a number or end: ")
    try:
        a = int(a)
        print(a)
    except:
        if a == "end":
            b = 1
        else:
            print("Invalid input")
print("Bye")


while True:
    ui = input("Wie viele Zahlen möchtest du generieren? ")
    try :
        ui = int(ui)
        break
    except ValueError:
        print("Bitte eine Zahl eingeben")
        continue

zahlen = []
for i in range(ui):
    zahlen.append(random.randint(1, 1000))


print("Die Zahlen sind:{}".format(zahlen))