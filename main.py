import turtle
from turtle import Screen
from snake import Snake
from food import Food
from gametext import GameText
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
text = GameText()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

text.write_score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food using turtle.distance()
    if snake.head.distance(food) < 15:
        food.refresh()
        text.update_score()


screen.exitonclick()