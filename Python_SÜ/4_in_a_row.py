'''
4 in a row in Python
Phillip
04.04.22
'''
import time

def display(list):
    # loop to make free space
    for x in range(50):
        print("")
    # own loop to display the playing field
    # diplays numbers on top of the playing field
    for x in range(7):
        print(" {}".format(x), end='')
    print()

    # creates the playing field
    for y in range(6):
        for x in range(7):
            # creates the playing field between the lines
            print("|{}".format(list[x][y]), end='')
        # creates the line between the rows
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

# defines a counter for the number of turns and y-coordinates for the chip
counter = 0
y_cord = 0
# defines a variable for the player so they can input their name
player_name_1 = input("Player 1, please enter your name: ")
player_name_2 = input("Player 2, please enter your name: ")
player = player_name_1
# defines a variable for the player so they can input their symbol
player_symbol_1 = input("{}, please enter your symbol: ".format(player_name_1))
player_symbol_2 = input("{}, please enter your symbol: ".format(player_name_2))
symbol = player_symbol_1
# defines a variable to store temporary values
was_taken = 0
was_out_of_range = 0

# main game loop starts here
while True:
    # displays the playing field
    display(playing_field)
    # asks the player to input a column
    x_cord = int(input("{} please enter column to drop your chip ->".format(player)))

    # display an error message if the field was out of range
    if (was_out_of_range == 1):
        print("You stupid ;) \nJust joking your coordinates are out of range, please try again!")

    # display an error message if the field was already taken
    if (was_taken == 1):
        print("This field is already taken!")

    # coordinates are on the playing_field
    if (x_cord >= 7 or x_cord < 0):
        # coordinates are not on the playing_field, store this data in a variable and restart the loop
        # so the player can enter a new value and the error message is displayed
        was_out_of_range = 1
        continue

    else:
        # check if this field is still free?
        if (playing_field[x_cord][y_cord] == ' '):
            # field is free
            playing_field[x_cord][y_cord] = symbol
        else:
            # field is already taken by someone, store this data in a variable and restart the loop
            # so the player can enter a new value and the error message is displayed
            was_taken = 1
            continue

    #reset the error variables
    was_out_of_range = 0
    was_taken = 0


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
            symbol = player_symbol_2
        else:
            player = player_name_1
            symbol = player_symbol_1
