'''
more functions
Phillip
28.03.22
'''

def spannungsteiler(r1,r2,u_ges):
    u1 = r1*(u_ges / (r1 + r2))
    u2 = r2*(u_ges / (r1 + r2))
    return (u1,u2)

def stromteiler(R1,R2,I_ges):
    I1 = I_ges*((1/(1/R1 + 1/ R2)) / R1)
    I2 = I_ges * ((1/(1/R1 + 1/ R2)) / R2)
    return (I1,I2)

### main part
print ("### Wilkommen zum Strom-/ Spannungsteiler rechnen ###")
while(True):
    x = int(input("Wollen Sie Strom- oder Spannungsteiler rechnen \n (für Strom drücken sie 1 für Spannungteiler 2) \n -> "))
    if (x == 1):
        r1 = int(input("Bitte R1 in k\u03A9 eingeben ->"))
        r2 = int(input("Bitte R2 in k\u03A9 eingeben ->"))
        Iges = int(input("Bitte Iges in A eingeben ->"))
        erg = spannungsteiler(r1, r2, Iges)
        print("I1={}A und I2={}A".format(erg[0], erg[1]))
        break

    elif (x == 2):
        r1 = int(input("Bitte R1 in k\u03A9 eingeben ->"))
        r2 = int(input("Bitte R2 in k\u03A9 eingeben ->"))
        u = int(input("Bitte Uges in V eingeben ->"))
        erg = spannungsteiler(r1,r2,u)
        print("U1={}V und U2={}V".format(erg[0],erg[1]))
        break

    else:
        print("Bitte geben sie eine gültige Zahl ein")