'''
4 in a row in Python
Phillip
04.04.22
'''
import time

def display(field):
    # loop to make free space
    for x in range(50):
        print("")
    # own loop to display the playing field
    # diplays numbers on top of the playing field
    for x in range(x_dim):
        print(" {}".format(x), end='')
    print()

    # creates the playing field
    for y in range(y_dim):
        for x in range(x_dim):
            # creates a row of lines between the playing field
            print("|{}".format(field[x][y]), end='')
        # creates the most left line and a vertical offset
        print("| ".format(y))

def check_for_win (x_cord,y_cord,field,symbol,y_dim,x_dim):
    def win_ceck(win):
        # checks if there is a win and resets if not
        if (win == 4):
            return True
        else:
            return False
    # go down and check if there is a symbol if not break
    win = 0
    print(x_cord,y_cord)
    for y in range(y_dim):
        if (field[x_cord][y] == symbol):
            win = win + 1
        else:
             break
    #checks if there is a win and resets if not
    win_state = win_ceck(win)
    if (win_state == True):
        return True
    win = 0
    # go up and check if there is a symbol if not break
    for y in range(y_dim-1,-1,-1):
        if (field[x_cord][y] == symbol):
            win = win + 1
        else:
            break

    #checks if there is a win and resets if not
    win_state = win_ceck(win)
    if (win_state == True):
        return True
    win = 0
    # go right and check if there is a symbol if not break
    for x in range(x_dim):
        if (field[x][y_cord] == symbol):
            win = win + 1
        else:
            break
    win_state = win_ceck(win)
    if (win_state == True):
        return True
    win = 0

    # go left and check if there is a symbol if not break
    for x in range(x_dim-1,-1,-1):
        if (field[x][y_cord] == symbol):
            win = win + 1
        else:
            break

    win_state = win_ceck(win)
    if (win_state == True):
        return True
    win = 0
    # go down-right and check if there is a symbol if not break
    for x in range(x_dim):
        for y in range(y_dim):
            if (field[x][y] == symbol):
                win = win + 1
            else:
                break
    win_state = win_ceck(win)
    if (win_state == True):
        return True
    win = 0
    # go down-left and check if there is a symbol if not break
    for x in range(x_dim):
        for y in range(y_dim):
            if (field[x][y] == symbol):
                win = win + 1
            else:
                break
    win_state = win_ceck(win)
    if (win_state == True):
        return True
    win = 0
    # go up-right and check if there is a symbol if not break
    for x in range(x_dim):
        for y in range(y_dim):
            if (field[x][y] == symbol):
                win = win + 1
            else:
                break
    win_state = win_ceck(win)
    if (win_state == True):
        return True
    win = 0
    # go up-left and check if there is a symbol if not break
    for x in range(x_dim):
        for y in range(y_dim):
            if (field[x][y] == symbol):
                win = win + 1
            else:
                break
    win_state = win_ceck(win)
    if (win_state == True):
        return True
    print(win_state)
    if (win_state == True):
        return True
    else:
        return False


def dropping_chip(x_cord,y_cord):
    # animation of dropping a chip
    while (True):
        # cancels the animation if the y cord is out of range
        if y_cord == 5:
            #stores the y_cord and ends the animation
            y_cord_old = y_cord
            return y_cord_old
        # moves the chip down and stores the previous y cord
        y_cord_old = y_cord
        y_cord = y_cord + 1
        # checks if a chip is on the field
        if (playing_field[x_cord][y_cord] == ' '):
            # displays the new playing field
            display(playing_field)
            # removes the chip from the previous y cord
            playing_field[x_cord][y_cord_old] = ' '
            # drops the chip on the new y cord
            playing_field[x_cord][y_cord] = symbol
            # waits for 0.5 seconds
            #time.sleep(0.5)
        else:
            y_cord_old = y_cord
            return y_cord_old

################################################################################
# Dimensions of the playing field
y_dim = 6
x_dim = 7
################################################################################

print("")
print("    ██╗  ██╗    ██╗███╗   ██╗     █████╗     ██████╗  ██████╗ ██╗    ██╗ ")
print("    ██║  ██║    ██║████╗  ██║    ██╔══██╗    ██╔══██╗██╔═══██╗██║    ██║ ")
print("    ███████║    ██║██╔██╗ ██║    ███████║    ██████╔╝██║   ██║██║ █╗ ██║ ")
print("    ╚════██║    ██║██║╚██╗██║    ██╔══██║    ██╔══██╗██║   ██║██║███╗██║ ")
print("         ██║    ██║██║ ╚████║    ██║  ██║    ██║  ██║╚██████╔╝╚███╔███╔╝ ")
print("         ╚═╝    ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝  ")
print("")

#### Main programm starts here ####
#creates the playing field and fills it with empty spaces (y_size = 6, x_size = 7)
playing_field = [[" " for y_size in range(y_dim)] for x_size in range(x_dim)]

# defines a counter for the number of turns and y-coordinates for the chip and the previous y-coordinate
counter = 0
y_cord = 0
x_cord = 0
y_cord_old = 0
field_size = x_dim * y_dim
# defines a variable for the player,so they can input their name
player_name_1 = input("Player 1, please enter your name: ")
player_name_2 = input("Player 2, please enter your name: ")
player = player_name_1
# defines a variable for the player, so they can input their symbol
player_symbol_1 = input("{}, please enter your symbol: ".format(player_name_1))
player_symbol_2 = input("{}, please enter your symbol: ".format(player_name_2))
symbol = player_symbol_1

# defines a variable to store temporary values
was_taken = 0
was_out_of_range = 0

#defines variables to store the chip position
x_pos = 0
y_pos = 0

# main game loop starts here
while True:

    # displays the playing field
    display(playing_field)

    # resets the y-coordinate to 0
    y_cord = 0

    # display an error message if the field was out of range
    if (was_out_of_range == 1):
        print("You stupid ;) \nJust joking your coordinates are out of range, please try again!")

    # display an error message if the field was already taken
    if (was_taken == 1):
        print("This field is already taken!")

    # asks the player to input a column
    x_cord = int(input("{} please enter the column to drop your chip in ->".format(player)))
    # coordinates are on the playing_field
    if (x_cord >= x_dim or x_cord < 0):
        # coordinates are not on the playing_field, store this data in a variable and restart the loop
        # so the player can enter a new value and the error message is displayed
        was_out_of_range = 1
        continue

    else:
        # check if this field is still free?
        if (playing_field[x_cord][y_cord] == ' '):
            # field is free
            #place the chip on the top of the column
            playing_field[x_cord][y_cord] = symbol
            # start the dropping animation
            y_cord_old =dropping_chip(x_cord,y_cord)
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
    if (counter == field_size):
        print("The game is a DRAW!")
        break

    display(playing_field)
    # check for win
    if (check_for_win(x_cord,y_cord_old,playing_field,symbol,y_dim,x_dim) == True):
        print("Congratulations {} you won !!!".format(player))
        break


    y_cord_old = 0
    # change player
    if (player == player_name_1):
        # if player 1 is the current player change to player 2
        player = player_name_2
        symbol = player_symbol_2
    else:
        # if player 2 is the current player change to player 1
        player = player_name_1
        symbol = player_symbol_1
