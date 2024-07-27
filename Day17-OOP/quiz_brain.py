class QuizBrain():
    def __init__(self, q_List):
        self.question_number = 0
        self.questions_list = q_List
        self.score = 0

    def next_question(self):
        curr_question = self.questions_list[self.question_number]
        correct_ans = curr_question.answer
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {curr_question.text }  (True/False)?:  ")
        self.check_answer(user_ans, correct_ans)
        print("\n")

    def check_answer(self,user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            self.score  += 1
            print("You got it right!")
        else:
            print("Oops, that's wrong")
        print(f"The correct answer was:  {corr_ans}.")
        print(f"Your current score is: {self.score} / {self.question_number} ")

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

        # try:
        #     chc = self.questions_list[self.question_number].text
        #     return True
        # except:
        #     return False


