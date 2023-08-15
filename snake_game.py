from turtle import Screen,Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard
from os import system
system("cls")
import time

limits = 281


screen = Screen()
screen.setup(width=600,height=600)
screen.title('The Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = 0

wall = Turtle()
wall.width(5)
wall.color("white")
wall.penup()
wall.goto(-295,295)
wall.pendown()
wall.goto(288,295)
wall.goto(288,-288)
wall.goto(-295,-288)
wall.goto(-295,295)

score_board = ScoreBoard(score)

screen.listen()
screen.onkey(snake.snake_up,"8")
screen.onkey(snake.snake_down,"2")
screen.onkey(snake.snake_left,"4")
screen.onkey(snake.snake_right,"6")

is_race_on = True
while is_race_on:
    screen.update()
    time.sleep(0.2)
    snake.snake_move()
    if snake.head.distance(food) < 15:
        print("mam mam")
        score+=1
        score_board.clear()
        score_board.new_score(score)
        food.refresh()
        snake.new_snake_segment()
    if snake.head.xcor() >= 284 or snake.head.xcor() <= -291 or snake.head.ycor() <= -288 or snake.head.ycor() >= 295:
        score_board.game_over()
        is_race_on = False
    is_this_snake_head = True
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
           score_board.game_over()
           is_race_on = False


screen.exitonclick()