import turtle
s = turtle.Screen()
s.bgcolor("black")
t = turtle.Turtle()
cellSize = 75

def drawBoard():
    t.speed(100)
    t.color("white")
    t.up()
    t.backward(225)
    t.left(90)
    t.forward(300)
    t.right(90)
    t.down()
    t.write("TIC TAC TOE: HOLIDAY EDITION", font=("Georgia", 36, "bold"))
    t.up()
    t.home()
    t.down()
    for i in range(2):
        t.left(90)
        t.up()
        t.forward((i+1)*cellSize)
        t.right(90)
        t.down()
        t.forward(3*cellSize)
        t.up()
        t.home()
    for j in range(2):
        t.forward((j + 1)* cellSize)
        t.left(90)
        t.down()
        t.forward(3*cellSize)
        t.up()
        t.home()
        
def drawX( cell):
    t.color("red")
    t.speed(100)
    t.up()
    t.home()
    t.forward(cellSize / 2 + cellSize * (cell % 3))
    t.left(90)
    t.forward((2.5 - (cell // 3)) * cellSize)
    t.down()
    t.left(45)
    t.forward(30)
    t.backward(60)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.backward(60)

def drawO( cell):
    t.color("green")
    t.speed(100)
    t.up()
    t.home()
    t.forward(cellSize*.88 + cellSize * (cell % 3))
    t.left(90)
    t.forward((2.5 - (cell // 3)) * cellSize)
    t.down()
    t.circle(30)

def gameOver(board):
    for n in range(3):
        value = board[n]
        value2 = board[n + 3]
        value3 = board[n + 6]
        if value != '*':
            if value == value2 == value3:
                if value == 'x' or value == 'o':
                    return True
    vertList = [0,3,6]
    for j in vertList:
        value = board[j]
        value2 = board[j + 1]
        value3 = board[j + 2]
        if value != '*':
            if value == value2 == value3:
                if value == 'x' or value == 'o':
                    return True
    if board[0] == board[4] == board[8] and board[0] != '*':
        return True
    if board[2] == board[4] == board[6] and board[2] != '*':
        return True
    return False

def isDraw(board):
    if '*' not in board:
        gameOver(board)
        if not gameOver(board):
            print('It is a draw!')
            return True
        else:
            return False

def drawLine(board, cellSize):
    t.width(3)
    t.color('navy')
    combinations = [(0, 4, 8), (2, 4, 6),  
                (0, 1, 2), (3, 4, 5), (6, 7, 8), 
                (0, 3, 6), (1, 4, 7), (2, 5, 8)] 
    diagonals = [(0, 4, 8), (2, 4, 6)] 
    rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]  
    columns = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]  
    for triplet in combinations:
        value1 = board[triplet[0]]
        value2 = board[triplet[1]]
        value3 = board[triplet[2]]
        if value1 == value2 == value3 and value1 != '*':
            if triplet in columns:
                winCol = triplet[0]
                t.up()
                t.home()
                t.forward((0.5 + winCol % 3) * cellSize)
                t.left(90)
                t.down()
                t.forward(3 * cellSize)
            if triplet in rows:
                winRow = triplet[0]
                t.up()
                t.home()
                t.left(90)
                t.forward((2.5 - winRow // 3) * cellSize)
                t.right(90)
                t.down()
                t.forward(3 * cellSize)
            if triplet == diagonals[0]:
                t.up()
                t.home()
                t.left(90)
                t.forward(3 * cellSize)
                t.right(135)
                t.down()
                t.forward(cellSize * 4)
            elif triplet == diagonals[1]:
                t.up()
                t.home()
                t.forward(3*cellSize)
                t.left(90)
                t.forward(3*cellSize)
                t.left(135)
                t.down()
                t.forward(4 * cellSize)
def drawWinner(winner):
    t.speed(100)
    t.color("white")
    t.up()
    t.home()
    t.right(90)
    t.forward(150)
    t.left(90)
    t.down()
    t.write(winner + " wins!", font=("Georgia",45, "italic"))
    
def playTTT():
    turtle.Screen()
    drawBoard()
    board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    playerX = input('Enter Name, Player X?: ')
    playerO = input('Enter Name, Player O? ')
    while not gameOver(board) and not isDraw(board):
        while True:
            xPos = input('X\'s turn ' + playerX + '? Enter a number from 0 to 8: ')
            xPos = int(xPos)
            try:
                if xPos < 0 or xPos > 8 or board[xPos] != '*':
                    print('You can\'t do that! Try again!')
                    continue
            except:
                print('You can\'t enter that number ! Please enter an integer from 0 to 8: ')
                continue
            else:
                break
        board[xPos] = 'x'
        drawX(xPos)
        gameOver(board)
        isDraw(board)
        if gameOver(board) :
            drawLine(board, cellSize)
            print('Player ' + playerX + ' has won! ')
            drawWinner(playerX)
            break
        elif isDraw(board):
            print('The game is a draw!')
            break
        while True:
            oPos = input('O\'s turn: ' + playerO + '? Enter a number from 0 to 8: ')
            oPos = int(oPos)
            try:
                if oPos < 0 or oPos > 8 or board[oPos] != '*':
                    print('You can\'t do that! Try again!')
                    continue
            except:
                print('You can\'t enter that number ! Please enter an integer from 0-8: ')
                continue
            else:
                break
        board[oPos] = 'o'
        drawO(oPos)
        gameOver(board)
        isDraw(board)
        if gameOver(board):
            drawLine(board, cellSize)
            print('Player ' + playerO + ' has won!')
            drawWinner(playerO)
            break
        elif isDraw(board):
            print('The game is a draw!')
            break
    print('Game Over')

playTTT()
