                    ######------SUDOKU SOLVER------######

''' The 0's in sudoku board are empty slots '''
GameBoard = [
             [7,8,0,4,0,0,1,2,0],
             [6,0,0,0,7,5,0,0,9],
             [0,0,0,6,0,1,0,7,8],
             [0,0,7,0,4,0,2,6,0],
             [0,0,1,0,5,0,9,3,0],
             [9,0,4,0,6,0,0,0,5],
             [0,7,0,3,0,0,0,1,2],
             [1,2,0,0,0,7,4,0,0],
             [0,4,9,2,0,6,0,0,7]
            ]


#this is the main funtion to solve sudoku board
def putNumbers(board):

    if not findEmptySlot(board):
        printTheBoard(board)
        return True

    position = findEmptySlot(board)
    
    for i in range(1,10):
         if isValid(board, i):
             board[position[0]][position[1]] = i
             if putNumbers(board):
                 return True
             else:   
                 board[position[0]][position[1]] = 0
                 
    return False
            
        

#this checks whether given number is valid for current slot
def isValid(board, number):

    position = findEmptySlot(board)
    boxX = position[1] // 3
    boxY = position[0] // 3

    #this is for checking vertical
    for i in range(len(board[position[0]])):
        if board[position[0]][i] == number :
            return False

    #tihs is for checking horizontal
    for i in range(len(board[position[0]])):
        if board[i][position[1]] == number:
            return False
        
    #this is for checking the little 3x3 box current slot lies in
    for i in range(boxY * 3, boxY * 3 + 3):
        
        for j in range(boxX * 3, boxX * 3 + 3):
            if board[i][j] == number:
                return False
        
    return True


#this is for findind the first empty slot in sudoku board
def findEmptySlot(board):

    for i in range(len(board)):
        
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
            
    return None
            

#this is only to printing out the sudoku board
def printTheBoard(board):

    for i in range(len(board)):        
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board[i])):
            if j%3 == 0 and j != 0:
                print("|", end = " " )

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")




print("  EMPTY GAME BOARD")
printTheBoard(GameBoard)
print("---------------------")
print("---------------------")
print("  FILLED GAME BOARD")
putNumbers(GameBoard)

