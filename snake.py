from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-21,0),(-41,0)]
MOVE_DISTANCE = 20

all_coordinates ={(0,0),(-21,0),(-41,0)}

class Snake:

    def __init__(self):
        self.segments = [] 
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        once = True
        for position in STARTING_POSITIONS:
            if once == True:
                new_segment = Turtle(shape='circle')
                # new_segment.shapesize(0.5,0.5)
                new_segment.color('yellow') 
                once = False
            else:
                new_segment = Turtle(shape='square')
                new_segment.shapesize(0.5,0.5)
                new_segment.color('yellow')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def snake_move(self):
        '''snake_move (speed of the snake from 0-1)'''
        #import time
        #time.sleep(speed)
        for seg_num in range(len(self.segments)-1,0,-1):
                now_x = self.segments[seg_num-1].xcor()
                now_y = self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(now_x,now_y)
        self.head.forward(MOVE_DISTANCE)


    def snake_up(self):
         if self.head.heading() != 270:
            self.head.setheading(90)
    def snake_down(self):
         if self.head.heading() != 90:
            self.head.setheading(270)
    def snake_left(self):
         if self.head.heading() != 0:
            self.head.setheading(180)
    def snake_right(self):
         if self.head.heading() != 180:
            self.head.setheading(0)

    def new_snake_segment(self):
        new_segment = Turtle(shape='square')
        new_segment.shapesize(0.5,0.5)
        new_segment.color('yellow')
        new_segment.penup()
        #new_segment.goto(self.segments[len(self.segments)-1])
        now_x = self.segments[len(self.segments)-1].xcor()
        now_y = self.segments[len(self.segments)-1].ycor()
        new_segment.goto(now_x,now_y)
        self.segments.append(new_segment)