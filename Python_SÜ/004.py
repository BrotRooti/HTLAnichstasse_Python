'''
Schleifen bzw. loops
Markus
10.01.2022
'''
#counter
x = 5

#while loops
while(x !=0):
    #solagne die Bedingung WAHR ist, wird
    #der code block ausgefuehrt
    print("Hello")
    x = x - 1

#loop bis user "end" eingibt
y = ""
while (y != "end"):
    y = input("Bitte was eingeben ->")
    if (y == "end"):
        break

#zahlen von 1 - 100
z = 1
while (z <= 100):
    print ("  ",z,end="")
    z= z + 1
print()
#for loop
for a in range(00,100,1):
    print(a)
