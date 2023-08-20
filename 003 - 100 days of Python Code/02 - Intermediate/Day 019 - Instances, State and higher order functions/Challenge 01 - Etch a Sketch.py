from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """Move the turtle forward"""
    tim.forward(10)


def move_backwards():
    """Move the turtle backwards"""
    tim.backward(10)


def turn_counter_clockwise():
    """Turn the turtle to the left"""
    tim.left(10)


def turn_clockwise():
    """Turn the turtle to the right"""
    tim.right(10)


def clear_screen():
    """Clear the screen and reset the position"""
    # tim.clear()
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
