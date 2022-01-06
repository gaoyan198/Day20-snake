from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()