import turtle
from turtle import Turtle
import time

MOVE_DISTANCE = 20
POSITION = [(0, 0), (-10, 0), (-20, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.my_turtles = []
        self.create_snake()


    def move(self):
        for seg in range(len(self.my_turtles) - 1, 0, -1):
            new_x = self.my_turtles[seg - 1].xcor()
            new_y = self.my_turtles[seg - 1].ycor()
            self.my_turtles[seg].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)
        self.head = self.my_turtles[0]

    def upward(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def downward(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color("white")
        self.my_turtles.append(new_turtle)

    def extend(self):

        self.add_segment(self.my_turtles[-1].pos())

    def collision(self):
        for i in range(1,len(self.my_turtles)):
            if self.my_turtles[0].pos()==self.my_turtles[i].pos():
                return True
            else:
                return False
    def reset(self):
        for snake in self.my_turtles:
            snake.goto(1000,1000)
        self.my_turtles.clear()
        self.create_snake()