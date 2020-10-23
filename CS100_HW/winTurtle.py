import turtle
class WinTurtle:
    def checkWin(grid):
        diags = ((0, 4, 8), (2, 4, 6))
        for n in range(3):
            test = grid[n]
            test2 = grid[n + 3]
            test3 = grid[n + 6]
            if test != '_':
                if test == test2 == test3:
                    if test == 'x' or test == 'o':
                        return True
        for j in range(0, 7, 3):
            test = grid[j]
            test2 = grid[j + 1]
            test3 = grid[j + 2]
            if test != '_':
                if test == test2 == test3:
                    if test == 'x' or test == 'o':
                        return True

        for tup in diags:
            test = grid[tup[0]]
            test2 = grid[tup[1]]
            test3 = grid[tup[2]]
            if test != '_':
                if test == test2 == test3:
                    return True
        return False

    def isDraw(grid):
        if '_' not in grid:
            TicTacToe.checkWin(grid)
            if not TicTacToe.checkWin(grid):
                print('It is a draw!')
                return True
            else:
                return False
            
    def drawLine(self, grid, cellsize, triplets, diags, rows, columns):
        for trip in triplets:
            test1 = grid[trip[0]]
            test2 = grid[trip[1]]
            test3 = grid[trip[2]]
            self.t.width(3)
            self.t.color('red')
            self.t.hideturtle()
            if test1 == test2 == test3 and test1 != '_':
                if trip in rows:
                    winRow = trip[0]
                    self.t.up()
                    self.t.home()
                    self.t.lt(90)
                    self.t.fd((2.5 - winRow // 3) * cellsize)
                    self.t.rt(90)
                    self.t.down()
                    self.t.fd(3 * cellsize)
                if trip in columns:
                    winCol = trip[0]
                    self.t.up()
                    self.t.home()
                    self.t.fd((0.5 + winCol % 3) * cellsize)
                    self.t.lt(90)
                    self.t.down()
                    self.t.fd(3 * cellsize)
                if trip == diags[0]:
                    self.t.up()
                    self.t.home()
                    self.t.lt(90)
                    self.t.fd(3 * cellsize)
                    self.t.rt(135)
                    self.t.down()
                    self.t.fd(cellsize * 4.5)
                elif trip == diags[1]:
                    self.t.up()
                    self.t.home()
                    self.t.fd(3*cellsize)
                    self.t.lt(90)
                    self.t.fd(3*cellsize)
                    self.t.lt(135)
                    self.t.down()
                    self.t.fd(4.5 * cellsize)
