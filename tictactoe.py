print("Hello, Welcome to TicTacToe by Hy")

val1 = int(input("Please enter your number of rows:"))
while val1 < 0:
    val1 = int(input("Number of rows should be greater than 0. Please enter again:"))
val2 = int(input("Please enter your number of columns:"))
while val2 < 0:
    val2 = int(input("Number of columns should be greater than 0. Please enter again:"))

numbers = int(input("How many number of points in one line a winner should have?"))
while numbers > val2 or numbers > val1 or numbers < 0:
    numbers = int(input("Please enter how many number of points in one line a winner should have again?"))


winnerSign = ""

board2d = t = [ [-1]*val2 for i in range(val1)]

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
            print("\n" + ' Y _' + "_____" * val2)
        else:
            print("\n" + '_____' + "_____" * val2)

def winner_checker():
    #check right cross
    for i in range(0,val2-numbers-1):
        if gotWinner == False:
            for j in range(0, val1-numbers-1):
                if gotWinner == False:
                    if check_availability(board2d[i][j])==False:
                        #print("Moc 1")
                        temp_x = i
                        temp_y = j
                        for g in range(0,numbers-1):
                            if(board2d[temp_x][temp_y] == board2d[temp_x+1][temp_y+1]):
                                #print("Moc 2")
                                temp_x = i+g+1
                                temp_y = i+g+1
                                if(temp_x >= i+numbers-1 ):
                                    #print("Moc 3")
                                    print(board2d[i][j])
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break
    #check left cross
    for i in range(numbers-1,val2):
        if gotWinner == False:
            for j in range(0, val1-numbers+1):
                if gotWinner == False:
                    if check_availability(board2d[i][j])==False:
                        #print("Moc 12")
                        temp_x = i
                        temp_y = j
                        for g in range(0,numbers-1):
                            if(board2d[temp_x][temp_y] == board2d[temp_x-1][temp_y+1]):
                                #print("Moc 22")
                                temp_x = i-g+1
                                temp_y = i+g+1
                                if(temp_x >= i-numbers+1 ):
                                    #print("Moc 3")
                                    print(board2d[i][j])
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
        print("Player 1 is the winner of this game!")
    else:
        print("Player 2 is the winner of this game!")

def ask_users1():
    inputx1 = int(input("Player 1! please enter position you want to mark: X="))
    while(inputx1>val2):
        inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
    inputy1 = int(input("                                                  Y="))
    while (inputy1 > val1):
        inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    while(check_availability(board2d[inputy1][inputx1])==False):
        inputx1 = int(input("Player 1! please enter position you want to mark: X="))
        while (inputx1 > val2):
            inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
        inputy1 = int(input("                                                  Y="))
        while (inputy1 > val1):
            inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    board2d[inputy1][inputx1] = 0

def ask_users2():
    inputx1 = int(input("Player 2! please enter position you want to mark: X="))
    while(inputx1>val2):
        inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
    inputy1 = int(input("                                                  Y="))
    while (inputy1 > val1):
        inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    while(check_availability(board2d[inputy1][inputx1])==False):
        inputx1 = int(input("Player 2! please enter position you want to mark: X="))
        while (inputx1 > val2):
            inputx1 = int(input("The x position you entered is invalid! please enter again: X="))
        inputy1 = int(input("                                                  Y="))
        while (inputy1 > val1):
            inputy1 = int(input("The y position you entered is invalid! please enter again: Y="))
    board2d[inputy1][inputx1] = 1

playerChoose= 0;
gotWinner = False
show_board()
while(gotWinner==False):
    if(playerChoose==0):
        ask_users1()
        show_board()
        winner_checker()
        playerChoose=1
    else:
        ask_users2()
        show_board()
        winner_checker()
        playerChoose=0


print(gotWinner)





