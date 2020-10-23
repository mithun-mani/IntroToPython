import turtle
class BoardTurtle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.cellsize = 100

    def drawBoard(self):
        for i in range(2):
            self.t.lt(90)
            self.t.up()
            self.t.fd((i + 1) * self.cellsize)
            self.t.rt(90)
            self.t.down()
            self.t.fd(3 * self.cellsize)
            self.t.up()
            self.t.home()
        for i in range(2):
            self.t.fd((i + 1) * self.cellsize)
            self.t.lt(90)
            self.t.down()
            self.t.fd(3 * self.cellsize)
            self.t.up()
            self.t.home()
        for n in range(9):
            self.t.up()
            self.t.home()
            self.t.fd(self.cellsize / 2 + self.cellsize * (n % 3))
            self.t.lt(90)
            self.t.forward((2.5 - (n // 3)) * self.cellsize)
            self.t.write(n)
