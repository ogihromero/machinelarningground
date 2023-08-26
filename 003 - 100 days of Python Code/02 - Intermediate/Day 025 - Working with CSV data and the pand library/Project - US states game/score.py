from turtle import Turtle

ALIGNMENT = "center"
FONT_ARIAL = ("Arial", 10, "normal")
FONT_OVER = ("Courier", 20, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()

    def write_state(self, answer, xcor, ycor):
        self.goto(xcor, ycor)
        self.write(f"{answer}", align=ALIGNMENT, font=FONT_ARIAL)

    def game_over(self, won_status):
        self.goto(0, 0)
        self.color("orange")
        if won_status:
            self.write(
                "You guessed all States, congratulations",
                align=ALIGNMENT,
                font=FONT_OVER,
            )
        else:
            self.write(
                "File with the missing states saved, you can check it out",
                align=ALIGNMENT,
                font=FONT_OVER,
            )
