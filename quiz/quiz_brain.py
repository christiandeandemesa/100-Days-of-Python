class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Creates a class method which are functions created objects can execute.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, answer):
        if answer.lower() == self.question_list[self.question_number].answer.lower():
            self.score += 1
            print("👍 You got the answer right!")
        else:
            print("👎 You got the answer wrong...")
    
        print(f"Your current score is: {self.score}/{len(self.question_list)}\n")
    
    def next_question(self):
        answer = input(f"Q{self.question_number}. {self.question_list[self.question_number].text} (True/False): ")
        self.check_answer(answer)
        self.question_number += 1