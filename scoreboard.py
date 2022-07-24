from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write("Liczba punktow {}".format(self.points), move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.points += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
