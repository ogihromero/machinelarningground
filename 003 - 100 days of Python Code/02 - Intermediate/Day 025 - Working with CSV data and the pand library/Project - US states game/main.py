import turtle
from os import path
import pandas as pd
from score import Score

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


# Function to get the directory of the path
# So files won't be read/written from the root directory (machinelarningground)
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


data = pd.read_csv(dir("50_states.csv"))

screen = turtle.Screen()
image = dir("blank_states_img.gif")
screen.addshape(image)
screen.title("US States Game")

turtle.shape(image)
turtle.penup()

answers = Score()
guessed_states: list[str] = []
while len(guessed_states) < 50:
    answer_state = str(
        screen.textinput(
            title=f"Guess the State {len(guessed_states)}/{len(data)}",
            prompt=("What State will you guess next? "
                    "Type 'exit'  whenever you want."),
        )
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in data["state"].values:
            if state not in guessed_states:
                missing_states.append(state)
        save_data = pd.DataFrame(missing_states)
        save_data.to_csv(dir("missed_states.csv"))
        break

    if (answer_state in data["state"].values) and (
        answer_state not in guessed_states
    ):
        state = data[data.state == answer_state]
        answers.write_state(
            answer=answer_state, xcor=int(state.x), ycor=int(state.y)
        )
        guessed_states.append(answer_state)

if len(guessed_states) == 50:
    answers.game_over(True)
else:
    answers.game_over(False)

# get click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
screen.exitonclick()
