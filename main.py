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
        snake.extent()
        text.update_score()
    # Detect Collision with wall if snake is too close to walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on  = False
        text.game_over()

    # Detect Collision with tail
    # if head collides with any tail segment, game over
    # can improve this with slicing
    for segment in snake.segments[1:]:
        # get the segments starting at 2
        # if segment == snake.head:
  #  code w/o slice       pass
        # elif
        if snake.head.distance(segment) < 10:
            text.game_over()
            game_is_on = False


screen.exitonclick()