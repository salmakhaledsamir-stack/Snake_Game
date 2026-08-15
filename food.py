from turtle import Turtle,Screen
from random import randrange


def random_color():
    r = randrange(0, 256)
    g = randrange(0, 256)
    b = randrange(0, 256)
    color = (r, g, b)
    return color


class Food(Turtle):

    def __init__(self):
        super().__init__()
        screen2=Screen()
        screen2.colormode(255)
        self.shape("turtle")
        self.penup()
        color=random_color()
        self.color(color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randrange(-280, 280)
        random_y = randrange(-280, 280)
        self.color(random_color())
        self.goto(random_x, random_y)