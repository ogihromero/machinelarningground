from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(
    title="Make your bet:", prompt=("Which turtle will win the race? pick a "
                                    + f"color: \n{(', '.join(colors))}"))

turtles: list[Turtle] = []
height = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed('slow')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=height)
    height += 40
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winner was the {winning_color} turtle")
            else:
                print(f"You lost! The winner was the {winning_color} turtle")
        move = random.randint(0, 10)
        turtle.forward(move)
screen.exitonclick()
