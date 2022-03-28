'''
Strukugramm Hausübung
28.02.22
Phillip H.

'''

import random

count = 1
würf_list = []


while (True):
    z1  = random.randint(1,6)
    z2  = random.randint(1,6)
    if (z1 and z2 == 6):
        break
    else:
        count = count + 1
        würf_var = "{}+{}".format(z1,z2)
        würf_list.append(würf_var)

print ("Es hat {} Versuche gebarucht.".format(count))
print()
print("Die Zahlen waren{}".format(würf_list))