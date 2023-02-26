import keyboard
import time
import random
import sys
import os


def play(M):
    x = 0
    y = 0
    alive = True
    while (alive):
        try:
            if keyboard.is_pressed('left'):
                x,y,M,alive = move(x,y,M,"left")
                time.sleep(0.5)
            elif keyboard.is_pressed('right'):
                x,y,M,alive = move(x,y,M,"right")
                time.sleep(0.5)
            elif keyboard.is_pressed('down'):
                x,y,M,alive = move(x,y,M,"down")
                time.sleep(0.5)
            elif keyboard.is_pressed('up'):
                x,y,M,alive = move(x,y,M,"up")
                time.sleep(0.5)
        except:
            break
    print("GAME OVER")


def move(x,y,M,move):
    x_aux = x
    y_aux = y
    if move == "left":
        y_aux -= 1
    elif move == "right":
        y_aux += 1
    elif move == "up":
        x_aux -= 1
    elif move == "down":
        x_aux += 1
    if validate_limits(x_aux, y_aux,M) :
        alive = True
        M[x][y] = 0
        if(M[x_aux][y_aux] == 2):
            return x,y,M,False
        else: 
            M[x_aux][y_aux] = 1
            M, alive = update_enemies(M)
            print_m(M)
            if x_aux == len(M)-1 :
                alive = False
                print("VICTORY!")
        return x_aux, y_aux, M, alive
    else:
        return x, y, M, True


def generate_enemies(M, rows, cols):
    for i in range(0, int(cols/3)):
        rand = random.randint(0,int(cols)-1)
        M[rows-1][rand] = 2
    return M


def update_enemies(M):
    rows = len(M)
    cols = len(M[0]) 

    for i in range(rows):
        for j in range(cols):
            if(M[i][j] == 2):
                M[i][j] = 0
                if(i>0):
                    if(M[i-1][j]==1):
                        return M, False
                    else:
                        M[i-1][j] = 2
    M = generate_enemies(M, rows, cols)
    return M, True



def validate_limits(x,y,M):
    if(x<len(M) and x>=0 and y<len(M[0]) and y>=0):
        return True


def print_m(M): 
    os.system("cls") 
    for i in range(len(M)):
        for j in range(len(M[i])):
            if(M[i][j] == 0):
                print("-",end=" ")
            elif(M[i][j] == 1):
                print("o",end=" ")
            elif(M[i][j] == 2):
                print("x",end=" ")
        print("")
    print()
    print("--------------------")

def set_dimetions():
    cols = input("Columns: ")
    rows = input("Rows: ")
    return cols, rows

def showw_menu():
    print()
    print("1. Set/Update dimentions")
    print("2. Play")
    print("3. Exit")
    option = input("Select an option: ")
    os.system("cls")
    return option


def main():
    os.system("cls")
    cols, rows = 7,8
    option = showw_menu()

    while(int(option) != 3):
        if int(option) == 1:
            cols, rows = set_dimetions()
        elif int(option) == 2:
            if int(cols) > 0 and int(rows) > 0 :
                M = [ [ 0 for j in range(int(cols))] for i in range(int(rows)) ] 
                M[0][0] = 1
                print_m(M)
                play(M)
            else:
                print("Invalid dimentions")
        option = showw_menu()




main()