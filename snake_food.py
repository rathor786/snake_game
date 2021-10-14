from turtle import Turtle
import random

FOOD_SIZE = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color('red')
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280,270 ), random.randint(-280, 270))
