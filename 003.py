'''
Drittes Übungsfile - Themen: User I/O und Verzweigungen
vorbereitung auf Taschenrechner HÜ
20.12.21
Phillip H.
'''

#als erstes den User nach zahlen und operator fragen
z1 = input("Bitte erste Zahl eingeben ->")
z1 = float(z1)
op = input("Bitte den Operator (+,-,*,/) eingeben ->")
z2 = float(input("Bitte die zweite Zahl eingeben ->"))

erg = 0.0
#if verzweigung
if (op == "+"):
    #dieser Block wird nur audgeführt wenn das if-statmen
    #wahr ist!!!
    erg = z1 + z2
if (op == "-"):
    erg= z1 - z2
if (op == "*"):
    erg = z1 * z2
if (op == "/"):
    erg = z1 / z2

print("Das Ergebnis lautet = {:.2f}".format(erg))