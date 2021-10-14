from turtle import Screen
import time
import snake
import snake_food
import scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

game_is_on = True
snake = snake.Snake()
food = snake_food.Food()

with open("data.txt","r") as file:

    a =int(file.read())
score = scoreboard.Scoreboard(a)


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(key="Up", fun=snake.upward)
    screen.onkey(key="Down", fun=snake.downward)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    if snake.head.distance(food)<15:
        food.refresh()
        score.refresh_score()
        snake.extend()

    #DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.collision() :
        score.reset()
        snake.reset()
        file1=open("data.txt","w")
        file1.write(str(score.high_score))
        file1.close()



   # DETECT IF HEAD COLLIDES WITH TAIL

screen.exitonclick()
