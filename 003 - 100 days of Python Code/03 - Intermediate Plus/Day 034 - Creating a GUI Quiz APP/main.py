from question_model import Question

# from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizzUI

parameters: dict[str, str | int] = {"amount": 10, "type": "boolean"}

response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()
question_bank = []
for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizzUI(quiz)
