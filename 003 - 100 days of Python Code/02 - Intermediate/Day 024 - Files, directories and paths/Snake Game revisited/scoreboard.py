from turtle import Turtle
from os import path

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Open from current directory
        with open(
            path.join(path.dirname(__file__), "data.txt"), "r"
        ) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def score_up(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} - High score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Open from current directory
            with open(
                path.join(path.dirname(__file__), "data.txt"), "w"
            ) as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
