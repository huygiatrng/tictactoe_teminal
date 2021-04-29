print("Hello, Welcome to TicTacToe by Hy")

val1 = input("Please enter your number of rows:")
val2 = input("Please enter your number of columns:")

val1 = int(val1)
val2 = int(val2)

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


show_board()
ask_users1()
show_board()

for i in range(len(board2d)):
    print(board2d[i])





