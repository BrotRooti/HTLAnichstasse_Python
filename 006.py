'''
Übunng zu Liste
31.01.22
Phillip
'''

#eine leere Liste anlegen
my_first_list = []

#eine vordefinierte Liste anlege
my_second_list = [1,2,3,5,7,9,'c',"hello 1bhel",3.1415]

print(my_second_list)
my_second_list[2] = 69
my_second_list.append("ich habe hunger")
print("my_second_list[2]={}".format(my_second_list[2]))

for x in my_second_list:
    print(x)