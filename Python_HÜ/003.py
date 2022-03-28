'''
Listen HÜ
31.01.22
Phillip
'''
#liste wird erstellt
list1 = []
x = 1
#design wird ausgegeben

print("------------------------------------------------")
print("|                Listen Programm               |")
print("|               Phillip  Hilscher              |")
print("------------------------------------------------")

#schleife
while(True):
    #im loop die Zahlen mit input einlesen und zur Liste mit append() anhängen
    y = input("Please input your {} number or end to stop: ".format(x))
    x = x + 1
    if (y == "end"):
        break
    else:
        y = int(y)
        list1.append(y)

#nach dem loop die liste mit .sort() sortieren und mit print() ausgeben
list1.sort()
print (list1)
print("The highest number was: {}".format(max(list1)))
print("")
print("The smallest number was: {}".format(min(list1)))
print("")