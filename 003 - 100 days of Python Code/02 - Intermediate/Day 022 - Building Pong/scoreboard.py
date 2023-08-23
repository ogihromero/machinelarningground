from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 150)
        self.update_score()

    def score_up(self, side):
        if side == "l":
            self.l_score += 1
        elif side == "r":
            self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score} - {self.r_score}",  align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",  align=ALIGNMENT,
                   font=FONT)
