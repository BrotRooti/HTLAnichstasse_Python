'''
Wiederholung der Python-Grundlagen
Phillip H.
10.01.2022
'''

eins = 12
zwei = 3.1415
drei = "Hello"
vier = False

#user output input
print("Guten Morgen, Guten Morgen 1BHEL!")
print("Der Wert von zwei = ",zwei)
print("zwei = {} und drei = {}".format(zwei,drei))

fuenf = input("Bitte eine Zahl eigeben ->")
print("fuenf hat den datentyP: ",type(fuenf))
fuenf = float(fuenf)
print("fuenf hat den datentyP: ",type(fuenf))

if (eins >10):
    print("eins ist größer als 10")
else:
    print("eins ist kleiner al 10")

x = int(input("Bitte eine Zahl (0-100) eingeben ->"))

if (x <=33):
    print("Deine Eingabe war kleiner gleich 33")
elif (x <= 66):
    print("Deine Eingabe war zwischen 34 und 66")
else:
    print("Deine Eingabe war zwischen 67 und 100")
