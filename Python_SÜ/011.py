'''
more functions
Phillip
28.03.22
'''

def spannungsteiler(r1,r2,u_ges):
    u1 = r1*(u_ges/(r1+r2))
    u2 = r2*(u_ges/(r1+r2))
    return (u1,u2)

### main part
print ("### Wilkommen zum Spannungsteiler rechnen ###")
r1 = int(input("Bitte R1 in k\u03A9 eingeben ->"))
r2 = int(input("Bitte R2 in k\u03A9 eingeben ->"))
u = int(input("Bitte Uges in V eingeben ->"))
erg = spannungsteiler(r1,r2,u)
print("U1={}V und U2={}V".format(erg[0],erg[1]))