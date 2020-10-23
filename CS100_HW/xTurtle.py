import turtle
class XTurtle:
    def __init__(self):
        self.t.down()
        self.t.lt(45)
        self.t.fd(30)
        self.t.backward(60)
        self.t.fd(30)
        self.t.rt(90)
        self.t.fd(30)
        self.t.backward(60)
        self.drawX(self, cell)

    def drawX(self, cell):
        self.t.up()
        self.t.home()
        self.t.fd(self.cellsize / 2 + self.cellsize * (cell % 3))
        self.t.lt(90)
        self.t.forward((2.5 - (cell // 3)) * self.cellsize)
        TicTacToe.anX(self)
