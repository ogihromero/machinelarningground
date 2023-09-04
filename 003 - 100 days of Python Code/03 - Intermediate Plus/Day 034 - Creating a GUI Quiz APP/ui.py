from tkinter import Tk, Canvas, PhotoImage, Label, Button
from os import path
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Ariel", 14, "italic")


# Current directory file path function
def dir(file_name):
    return path.join(path.dirname(__file__), file_name)


class QuizzUI:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(
            text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white"
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            (150, 125), width=280, text="", fill=THEME_COLOR, font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file=dir("images/true.png"))
        false_img = PhotoImage(file=dir("images/false.png"))

        self.true_button = Button(
            image=true_img, bg=THEME_COLOR, border=0, command=self.check_true
        )
        self.true_button.grid(row=2, column=1)

        self.false_button = Button(
            image=false_img, bg=THEME_COLOR, border=0, command=self.check_false
        )
        self.false_button.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've completed the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback("True")

    def check_false(self):
        self.give_feedback("False")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, answer):
        if self.quiz.check_answer(answer):
            self.update_score()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)
