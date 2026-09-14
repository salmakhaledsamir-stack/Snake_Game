from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time


screen=Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)

screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

screen.onkey(key="w",fun=snake.up)
screen.onkey(key="s",fun=snake.down)
screen.onkey(key="a",fun=snake.left)
screen.onkey(key="d",fun=snake.right)



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        score.score_increase()
        snake.extend()

    if snake.head.xcor()>390 or snake.head.ycor()>390 or snake.head.xcor()<-390 or snake.head.ycor()<-390:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()

screen.exitonclick()