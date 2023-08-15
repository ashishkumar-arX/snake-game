from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,score):
        super().__init__(visible=False)
        self.speed("fastest")
        self.color('white')
        self.score = score
        self.penup()
        self.goto(0,260)
        self.new_score(self.score)

    def new_score(self,new_score):
        self.score = new_score
        self.write(f'Your score is {self.score}',align='center',font=("Arial",15,"normal"))

    def game_over(self):
        self.home()
        self.write(f'GAME OVER',align='center',font=("Arial",40,"normal"))