'''
4 in a row in Python
Phillip
04.04.22
'''
import time

def display(list):
    #loop to make free space
    for x in range(50):
        print("")
    # own loop to display the playing field
    for x in range(7):
        print(" {}".format(x), end='')
    print()

    for y in range(6):
        for x in range(7):
            print("|{}".format(list[x][y]), end='')
        print("| ".format(y))


def check_for_win():
    # if a player has 3 in a row or diagonal then return 1
    # else return 0
    for row in range(0, 3, 1):
        if (playing_field[0][row] == playing_field[1][row] == playing_field[2][row] != " "):
            return 1
        elif (playing_field[row][0] == playing_field[row][1] == playing_field[row][2] != " "):
            return 1
    if (playing_field[0][0] == playing_field[1][1] == playing_field[2][2] != " "):
        return 1
    elif (playing_field[2][0] == playing_field[1][1] == playing_field[0][2] != " "):
        return 1
    return 0

def check_for_tie():
    # if all fields are filled then return 1
    # else return 0
    for row in range(0, 3, 1):
        for column in range(0, 3, 1):
            if (playing_field[row][column] == " "):
                return 0
    return 1

def dropping_chip():
    # animation of dropping a chip
    for x in range(6):
        for y in range(7):
            print("|{}".format(playing_field[y][x]), end='')



print("")
print("    ██╗  ██╗    ██╗███╗   ██╗     █████╗     ██████╗  ██████╗ ██╗    ██╗ ")
print("    ██║  ██║    ██║████╗  ██║    ██╔══██╗    ██╔══██╗██╔═══██╗██║    ██║ ")
print("    ███████║    ██║██╔██╗ ██║    ███████║    ██████╔╝██║   ██║██║ █╗ ██║ ")
print("    ╚════██║    ██║██║╚██╗██║    ██╔══██║    ██╔══██╗██║   ██║██║███╗██║ ")
print("         ██║    ██║██║ ╚████║    ██║  ██║    ██║  ██║╚██████╔╝╚███╔███╔╝ ")
print("         ╚═╝    ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝  ")
print("")

#### Main programm starts here ####
playing_field = [[" " for i in range(6)] for j in range(7)]

# variables which we will need
counter = 0
player_name_1 = input("Player 1, please enter your name: ")
player_name_2 = input("Player 2, please enter your name: ")
player = player_name_1
symbol = 'X'

# main game loop starts here
while True:
    display(playing_field)
    x_cord = int(input("{} please enter column to drop your chip ->".format(player)))

    # coordinates are on the playing_field
    if (x_cord >= 7 or x_cord < 0):
        print("You stupid ;) \nJust joking your coordinates are out of range, please try again!")
        continue

    else:
        # check if this field is still free?
        if (playing_field[x_cord][y_cord] == ' '):
            # field is free
            playing_field[x_cord][y_cord] = symbol
        else:
            print("This field is already taken!")
            continue

        # display the playing_field
        display(playing_field)

        # update counter
        counter = counter + 1

        # check for draw
        if (counter == 9):
            print("The game is a DRAW!")
            break

        # check for win
        if (check_for_win()):
            print("Congratulations {} you won !!!".format(player))
            break

        # change player
        if (player == player_name_1):
            player = player_name_2
            symbol = 'O'
        else:
            player = player_name_1
            symbol = 'X'
