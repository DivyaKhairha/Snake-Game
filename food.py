import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid = 0.75,stretch_len = 0.75)
        self.color("white")
        self.penup()
        

    def refresh(self):
        self.goto(x = random.randint(-290,290),y = random.randint(-190,170))
        

