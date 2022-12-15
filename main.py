theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("\nGuide of the positions on the board:\n")
    print("7 | 8 | 9")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("1 | 2 | 3")


def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("\nIt's your turn: " + turn + "! Enter the number of the place you would like to move to on the board. What's your move?\n")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to another spot?")
            continue

        
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\n**** Game Over. ****\n")                
                print(" **** " +turn + " WON! ****")
                break 

        
        if count == 9:
            print("\n**** Game Over. ****\n")                
            print("It's a TIE!!")
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        

    
    restart = input("\nDo want to play Again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()  

if __name__ == "__main__":
    game()