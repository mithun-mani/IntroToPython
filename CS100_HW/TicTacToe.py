class TicTacToe:
    def __init__(self):
        triplets = ((0, 4, 8), (2, 4, 6),  # these are diagonals
                    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # these are rows
                    (0, 3, 6), (1, 4, 7), (2, 5, 8))  # these are columns
        diags = ((0, 4, 8), (2, 4, 6))  # these are diagonals
        rows = ((0, 1, 2), (3, 4, 5), (6, 7, 8))  # these are rows
        columns = ((0, 3, 6), (1, 4, 7), (2, 5, 8))  # these are columns
        grid = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        playerX = input('Who is Player X? ')
        playerO = input('Who is Player O? ')
        turtle.Screen()
        TicTacToe.drawGrid(self)

    while not TicTacToe.checkWin(grid) and not TicTacToe.isDraw(grid):
        while True:
            placeX = input('where do you want to place your X ' + playerX + '? Enter integer 0-8 ')
            try:
                if int(placeX) < 0 or int(placeX) > 8 or grid[int(placeX)] != '_':
                    print('Invalid, try again!')
                    continue
            except:
                print('Invalid entry! Please enter an integer from 0-8! ')
                continue
            else:
                break
        cell = int(placeX)
        grid[cell] = 'x'
        TicTacToe.drawX(self, cell)
        TicTacToe.checkWin(grid)
        TicTacToe.isDraw(grid)
        if TicTacToe.checkWin(grid) :
            TicTacToe.drawLine(self, grid, 100, triplets, diags, rows, columns)
            print('Player ' + playerX + ' has won! ')
            break
        elif TicTacToe.isDraw(grid):
            print('Alas, it is but a draw :/')
            break
        while True:
            placeO = input('where do you want to place your O ' + playerO + '? Enter integer 0-8. ')
            try:
                if int(placeO) < 0 or int(placeO) > 8 or grid[int(placeO)] != '_':
                    print('Invalid, try again')
                    continue
            except:
                print('Invalid entry! Please enter an integer from 0-8! ')
                continue
            else:
                break
        cell = int(placeO)
        grid[cell] = 'o'
        TicTacToe.drawO(self, cell)
        TicTacToe.checkWin(grid)
        TicTacToe.isDraw(grid)
        if TicTacToe.checkWin(grid):
            TicTacToe.drawLine(self,grid, 100, triplets, diags, rows, columns)
            print('Player ' + playerO + ' has won!')
            break
        elif TicTacToe.isDraw(grid):
            print('Alas, it is but a draw :/')
            break
    print('Game Over')
        
