from turtle import Turtle

BLOCK_IN_THE_MIDDLE = []
NUM_LIST = 15


def create_lines(y=280):
    for i in range(NUM_LIST):
        sum_cor = (0, y)
        BLOCK_IN_THE_MIDDLE.append(sum_cor)
        y -= 40
    for pivot in range(NUM_LIST):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.speed("fastest")
        new_turtle.shapesize(0.7)
        new_turtle.goto(BLOCK_IN_THE_MIDDLE[pivot])


class ScreenSettings(Turtle):
    def __init__(self):
        super().__init__()
        create_lines()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        style = ("Courier", 70, "normal")
        self.write(self.l_score, align="center", font=style)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=style)

    def l_block_score(self):
        self.l_score += 1
        self.update_score()

    def r_block_score(self):
        self.r_score += 1
        self.update_score()

    def who_wins(self):
        if self.l_score == 5:
            self.goto(0, 0)
            style = ("Courier", 70, "normal")
            self.write("Left won!", align="center", font=style)
            return False
        elif self.r_score == 5:
            self.goto(0, 0)
            style = ("Courier", 70, "normal")
            self.write("Right won!", align="center", font=style)
            return False
        else:
            return True
