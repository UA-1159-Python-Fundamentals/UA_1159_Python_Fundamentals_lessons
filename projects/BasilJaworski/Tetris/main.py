import os
import pygame

from random import randint
from time import sleep

pygame.init()

res_x = 15
res_y = 10

screen_pixel_damaged = "O"

fig1 = [[0, 1], [0, 2], [1, 0], [1, 1]] #revers
fig2 = [[0, 0], [0, 1], [0, 2], [0, 3]] #line
fig3 = [[0, 0], [1, 0], [1, 1], [1, 2]] #letter L
fig4 = [[0, 1], [1, 0], [1, 1], [1, 2]] #tripple
fig5 = [[0, 0], [0, 1], [1, 0], [1, 1]] #rect

screen = list([" " for i in range(res_y)] for k in range(res_x))
screen_damage = list([" " for i in range(res_y)] for k in range(res_x))

def write_main_object(x, y):
    """Displaying. Draw the main object on the screen"""

    if main_obj == 1:
        for i, k in fig1:
            screen[i+x][k+y] = "0"
    elif main_obj == 2:
        for i, k in fig2:
            screen[i+x][k+y] = "0"
    elif main_obj == 3:
        for i, k in fig3:
            screen[i+x][k+y] = "0"
    elif main_obj == 4:
        for i, k in fig4:
            screen[i+x][k+y] = "0"
    elif main_obj == 5:
        for i, k in fig5:
            screen[i+x][k+y] = "0"

def obj_form():
    """Information. Returns points of current figure"""

    fig_t = []
    if main_obj == 1:
        fig_t = fig1.copy()
    elif main_obj == 2:
        fig_t = fig2.copy()
    elif main_obj == 3:
        fig_t = fig3.copy()
    elif main_obj == 4:
        fig_t = fig4.copy()
    elif main_obj == 5:
        fig_t = fig5.copy()
    return fig_t

def touch_obj():
    """Information. Returns coordinates of points of current figure"""

    fig_t = []
    if main_obj == 1:
        for i in fig1:
            fig_t.append([i[0]+obj_x, i[1]+obj_y])
    elif main_obj == 2:
        for i in fig2:
            fig_t.append([i[0]+obj_x, i[1]+obj_y])
    elif main_obj == 3:
        for i in fig3:
            fig_t.append([i[0]+obj_x, i[1]+obj_y])
    elif main_obj == 4:
        for i in fig4:
            fig_t.append([i[0]+obj_x, i[1]+obj_y])
    elif main_obj == 5:
        for i in fig5:
            fig_t.append([i[0]+obj_x, i[1]+obj_y])
    return fig_t


def touch_wall(wall):
    """Physic. Returns True if object touching one of the walls"""

    if wall == 'left':
        obj_left = []
        for i in touch_obj():
            if [i[0], i[1]-1] not in touch_obj():
                obj_left.append(i)
        for i in obj_left:
            if i[1] == 0 or screen_damage[i[0]][i[1]-1] == screen_pixel_damaged: 
                return True
        return False
    elif wall == 'right':
        obj_right = []
        for i in touch_obj():
            if [i[0], i[1]+1] not in touch_obj():
                obj_right.append(i)
        for i in touch_obj():
            if i[1] == res_y-1 or screen_damage[i[0]][i[1]+1] == screen_pixel_damaged: 
                return True
        return False
    
def touch_flour():
    """Physic. Returns True if one of the object points touching the flour"""

    #For define bottom points of the figure
    obj_bot = []
    for i in touch_obj():
        if [i[0]+1, i[1]] not in touch_obj():
            obj_bot.append(i)
    
    for i in obj_bot:
        if i[0] == res_x-1 or screen_damage[i[0]+1][i[1]] == screen_pixel_damaged:
            return True
    return False
    
def new_obj():
    """Calculating. Moves main object to the start and randome it"""

    global main_obj, obj_x, obj_y
    main_obj = randint(1, 5)
    obj_x = 0
    obj_y = 4

def rem_damage():
    """Calculating. Adds the landed object to another not awailable points on the screen"""

    for i in touch_obj():
        screen_damage[i[0]][i[1]] = screen_pixel_damaged

def rot_obj():
    """The function returns coordinates of points of the figure rotated by 90deg."""

    global fig1,fig2,fig3,fig4,fig5
    mat_obg = []
    mat_x = 0
    mat_y = 0

    #Finding sizes of matrix
    for i in obj_form():
        if i[0] > mat_x:
            mat_x = i[0]
    for i in obj_form():
        if i[1] > mat_y:
            mat_y = i[1]
    mat_x += 1
    mat_y += 1

    #Transforming coordinates in to the matrix
    for i in range(mat_x):
        mat_line = []
        for n in range(mat_y):
            if [i, n] in obj_form():
                mat_line.append(True)
            else:
                mat_line.append(False)
        mat_obg.append(mat_line)
    
    #Rotating the matrix
    mat_rot = []
    print()
    for i in range(mat_y):
        mat_rot_line = []
        for k in mat_obg:
            mat_rot_line.append(k[mat_y-1])
        mat_rot.append(mat_rot_line)
        mat_y -= 1
        
    #Transforming the matrics in to the coordinates
    c_x = 0
    c_y = 0 
    rotated_obj = []
    for i in mat_rot:
        c_y = 0
        for k in i:
            if k == True:
                rotated_obj.append([c_x, c_y])
            c_y += 1
        c_x += 1
    
    return rotated_obj
            
            

def clr_screen():
    """Displaying and Calculating. Clear the console and screen"""

    global screen
    os.system('clear')
    screen = list([" " for i in range(res_y)] for k in range(res_x))

def shw_screen():
    """Displaying. The render function, add all objects on the screen and draws it"""

    os.system('clear')

    for i in range(res_x):
        for k in range(res_y):
            screen[i][k] = screen_damage[i][k]

    write_main_object(obj_x, obj_y)

    for i in range(res_x):
        for k in range(res_y):
            print(screen[i][k], end="")
        print()

def checker_bonus():
    """Calculating. Checks if there are full lines, removes it and gives the bonuses)"""

    global score
    for i in range(res_x-1, 0, -1):
        counter = 0
        for k in screen_damage[i]:
            if k == screen_pixel_damaged:
                counter += 1
        if counter == res_y:
            score += 1
            for ii in range(i, 0, -1):
                screen_damage[ii] = screen_damage[ii-1]

def lose():
    """Calculating. Checks if the objects almoust at the top of the screen"""

    for i in screen_damage[2]:
        if i == screen_pixel_damaged:
            return True
    return False


game = False
start_screen = True

counter = 0
main_clock = 0
score = 0

new_obj()

#The start screen
while start_screen:
    print("Hey! Let's play the TETRIS!")
    print("Enter--> 1 if you want to play")
    print("Enter--> 0 if you want to quit")
    user_choise = input("Here: ")
    if user_choise == "1":
        game = True
        start_screen = False
    elif user_choise == "0":
        quit()

#The game screen
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.unicode == "a" and touch_wall('left') == False:
                obj_y -= 1
            elif event.unicode == "d" and touch_wall('right') == False:
                obj_y += 1
            elif event.unicode == "w":
                if main_obj == 1:
                    fig1 = rot_obj()
                elif main_obj == 2:
                    fig2 = rot_obj()
                elif main_obj == 3:
                    fig3 = rot_obj()
                elif main_obj == 4:
                    fig4 = rot_obj()
                elif main_obj == 5:
                    fig5 = rot_obj()
                elif event.unicode == "s":
                    if touch_flour() == False:
                        obj_x += 1
            elif event.unicode == "\x08":
                quit()

    if main_clock%20 == 0:
        touch = touch_flour()
        if touch == False:
            obj_x += 1
        elif touch == True:
            rem_damage()
            new_obj()
            counter += 1

        
        
    shw_screen()
    checker_bonus()

    main_clock += 1
    print(f"Your score is: {score}")

    sleep(0.01)
    
    if lose():
        print(f"Sorry you lose with score: {score}")
        game = False

    if main_clock == 100:
        main_clock = 1
        print(main_clock)