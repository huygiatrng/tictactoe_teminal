import os

print("Hello, Welcome to TicTacToe by Huy")

row = int(input("Please enter your number of rows:"))
while row < 0:
    row = int(input("Number of rows should be greater than 0. Please enter again:"))
column = int(input("Please enter your number of columns:"))
while column < 0:
    column = int(input("Number of columns should be greater than 0. Please enter again:"))

numbers = int(input("How many number of points in one line a winner should have?"))
while numbers > column or numbers > row or numbers < 0:
    numbers = int(input("Please enter how many number of points in one line a winner should have again?"))


winnerSign = ""

board2d = t = [ [-1]*column for i in range(row)]

def check_value(x):
    if x == -1:
        return "   "
    elif x == 0:
        return " O "
    else:
        return " X "

def check_availability(x):
    if x == -1:
        return True
    else:
        return False

def show_board():
    print('_____',end="")
    for i in range(len(board2d[0])):
        print("["+f'{i:2.0f}'+"]_", end = "")
    print("X")
    for i in range(len(board2d)):
        print("["+f'{i:2.0f}'+"]|", end=" ")
        for j in range(len(board2d[i])):
            print(check_value(board2d[i][j]) + "|", end=" ")
        if(i==len(board2d)-1):
            print("\n" + ' Y _' + "_____" * column)
        else:
            print("\n" + '_____' + "_____" * column)

def winner_checker():
    #check diagonal left
    for i in range(0,row-numbers+1):
        if gotWinner == False:
            for j in range(0, column-numbers+1):
                if gotWinner == False:
                    if check_availability(board2d[i][j])==False:
                        counter = 0
                        temp_y = i
                        temp_x = j
                        for g in range(0,numbers-1):
                            if(board2d[temp_y][temp_x] == board2d[temp_y+1][temp_x+1]):
                                temp_y +=1
                                temp_x +=1
                                counter += 1
                                if(counter>=numbers-1):
                                    print(board2d[i][j])
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break
    #check diagonal right
    for i in range(0,row-numbers+1):
        if gotWinner == False:
            for j in range(numbers-1,column):
                if gotWinner == False:
                    if check_availability(board2d[i][j])==False:
                        temp_y = i
                        temp_x = j
                        counter = 0
                        for g in range(0,numbers-1):
                            if(board2d[temp_y][temp_x] == board2d[temp_y+1][temp_x-1]):
                                temp_y +=1
                                temp_x -=1
                                counter+=1
                                if(counter>=numbers-1 ):
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break
    #check vertical line
    for i in range(0,row-numbers+1):
        if gotWinner == False:
            for j in range(0,column):
                if gotWinner == False:
                    if check_availability(board2d[i][j])==False:
                        temp_y = i
                        temp_x = j
                        counter = 0
                        for g in range(0,numbers-1):
                            if(board2d[temp_y][temp_x] == board2d[temp_y+1][temp_x]):
                                temp_y +=1
                                counter+=1
                                if(counter>=numbers-1 ):
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break
    #check horizontal line
    for i in range(0,row):
        if gotWinner == False:
            for j in range(0,column-numbers+1):
                if gotWinner == False:
                    if check_availability(board2d[i][j])==False:
                        temp_y = i
                        temp_x = j
                        counter = 0
                        for g in range(0,numbers-1):
                            if(board2d[temp_y][temp_x] == board2d[temp_y][temp_x+1]):
                                temp_x +=1
                                counter+=1
                                if(counter>=numbers-1 ):
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break


def printWinner(winnerSign):
    global gotWinner
    gotWinner = True
    if(winnerSign == 0):
        print("\nPlayer 1 is the winner of this game!")
        inputt = input("")
    else:
        print("\nPlayer 2 is the winner of this game!")
        inputt = input("")

def ask_users1():
    inputx1 = int(input("Player 1! please enter position you want to mark: X="))
    while(inputx1>column):
        inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
    inputy1 = int(input("                                                  Y="))
    while (inputy1 > row):
        inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    while(check_availability(board2d[inputy1][inputx1])==False):
        inputx1 = int(input("Player 1! please enter position you want to mark: X="))
        while (inputx1 > column):
            inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
        inputy1 = int(input("                                                  Y="))
        while (inputy1 > row):
            inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    board2d[inputy1][inputx1] = 0

def ask_users2():
    inputx1 = int(input("Player 2! please enter position you want to mark: X="))
    while(inputx1>column):
        inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
    inputy1 = int(input("                                                  Y="))
    while (inputy1 > row):
        inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    while(check_availability(board2d[inputy1][inputx1])==False):
        inputx1 = int(input("Player 2! please enter position you want to mark: X="))
        while (inputx1 > column):
            inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
        inputy1 = int(input("                                                  Y="))
        while (inputy1 > row):
            inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    board2d[inputy1][inputx1] = 1

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hello, Welcome to TicTacToe by Huy")
    print("Please enter your number of rows:"+str(row))
    print("Please enter your number of columns:"+str(column))
    print("How many number of points in one line a winner should have?"+str(numbers))

playerChoose= 0;
gotWinner = False
show_board()
while(gotWinner==False):
    if(playerChoose==0):
        ask_users1()
        clean_terminal()
        show_board()
        winner_checker()
        playerChoose=1
    else:
        ask_users2()
        clean_terminal()
        show_board()
        winner_checker()
        playerChoose=0


print(gotWinner)





