'''
Taschenrechner HÜ
20.12.21
Phillip H.
'''
print("------------------------------------------------")
print("|             Taschenrechner V1.0              |")
print("|               Phillip Hilscher               |")
print("------------------------------------------------")

#start des Rechners
reset1 = "y"
while (reset1 == "y"):
    
    #als erstes den User nach zahlen und operator fragen
    z1 = float(input("Bitte die erste Zahl eingeben ->"))
    op = input("Bitte die Rechenoperation (+,-,*,/) auswählen ->")
    z2 = float(input("Bitte die zweite Zahl eingeben ->"))

    erg = 0.0
    #if verzweigung
    if (op == "+"):
        #dieser Block wird nur audgeführt wenn das if-statmen
        #wahr ist!!!
        erg = z1 + z2
    elif (op == "-"):
        erg= z1 - z2
    elif (op == "*"):
        erg = z1 * z2
    else:
        erg = z1 / z2

    print("Das Ergebnis lautet = {:.2f}".format(erg))

    #weitere Rechenoperation?
    reset1 = input("Wollen Sie ein weitere Zahl berechne? (y,n) ->")
if not (reset1 == "y"):
    print("Dann noch eine schönen Tag")
    print("Auf Wiedersehen")
