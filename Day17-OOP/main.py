from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
##
question_bank = []
for q in question_data:
    # print(q["text"])
    text = q["text"]
    ans =  q["answer"]
    obj = Question(text,ans)
    question_bank.append(obj)
##
# print(question_bank[10].text)
quiz= QuizBrain(question_bank)
while (quiz.still_has_questions()):
    quiz.next_question()
print("\n")
print("***********************")
print("You completed the quiz")
print(f"You got a final score of {quiz.score}/12 ")
print("***********************")
