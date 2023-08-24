from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        # self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-190, 250)
        self.update_level()

    def level_up(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}",  align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",  align=ALIGNMENT,
                   font=FONT)
