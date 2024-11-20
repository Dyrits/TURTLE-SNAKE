from random import choice
import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

def loop():
    global speed
    snake.move()
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390 or snake.collide():
        scoreboard.game_over()
        return
    if snake.head.distance(food) < 15:
        scoreboard.increase()
        food.refresh()
        snake.grow()
        speed = max(5, speed - 5)  # Ensure speed doesn't go below 5 milliseconds
    screen.update()
    screen.ontimer(loop, speed)  # Schedule the next call

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.title("Snake")
    screen.tracer(0)
    food = Food()
    scoreboard = Scoreboard()
    snake = Snake()
    screen.update()
    speed = 1000
    screen.onkey(lambda: [snake.up(), snake.move(), screen.update()], "Up")
    screen.onkey(lambda: [snake.down(), snake.move(), screen.update()], "Down")
    screen.onkey(lambda: [snake.right(), snake.move(), screen.update()], "Right")
    screen.onkey(lambda: [snake.left(), snake.move(), screen.update()], "Left")
    screen.listen()
    loop()  # Start the game loop
    screen.mainloop()