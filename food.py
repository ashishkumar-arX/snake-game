from turtle import Turtle
from random  import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("blue")
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.penup()
        self.refresh()
    
    def refresh(self):
        x_coordinate = randint(-260,260)
        y_coordinate = randint(-260,260)
        self.goto(x_coordinate,y_coordinate)