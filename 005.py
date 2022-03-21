'''
Übung zu Funktionen
24.01.22
Phillip
'''

def my_parallel_calc(a,b):
    r_ges = a*b/(a+b)
    return r_ges

print("Wilkommen zum Parallel-Wiederstand-Berechnen ###")
rp = "y"

while (rp == "y"):
    r1 = float(input("Bitte den Wert von R1 in k\u03A9 eingeben -> "))
    r2 = float(input("Bitte den Wert von R2 in kΩ eingeben -> "))

    print("R_ges= {}".format(my_parallel_calc(r1,r2)))
    print("")
    #wiederholung
    rp = input("Soll noch eine Zahl berechnet werden? (y,n): ")
    if not (rp == "y"):
        print("Danke fürs benutzen")
        break
    