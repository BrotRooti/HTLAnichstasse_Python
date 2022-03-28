'''
Zweite Hausübung
Frag den User nach einer Start- und Endzahl und einer Schrittweite. Und gibt die so spezifizierte Zahlenfolge aus. Eine Zahl pro Zeile!
Phillip
10.01.2022
'''
x = int(input("Bitte eine Startzahl eingeben ->"))
y = int(input("Bitte eine Endzahl eingeben ->"))
z = int(input("Bitte eine Schrittgröße eingeben ->"))

a = y + z

for b in range(x,a,z):
 print(b)
