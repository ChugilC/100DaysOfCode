from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
print("Welcome to the Quiz")
for question in question_data:
    new_ques = Question(question['text'], question['answer'])
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")