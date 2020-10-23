class OTurtle:
     def __init__(self):
        self.t.down()
        self.t.circle(30)

    def drawO(self, cell):
        self.t.up()
        self.t.home()
        self.t.fd(self.cellsize * 0.75 + self.cellsize * (cell % 3))
        self.t.lt(90)
        self.t.forward((2.5 - (cell // 3)) * self.cellsize)
        TicTacToe.anO(self)
