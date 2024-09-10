import turtle as t
import time


class Snake:
    def __init__(self):
        self.list_tut = []
        self.create_snake()

    def create_snake(self):
        for i in range(10):
            temp = t.Turtle()
            temp.speed(1)
            temp.penup()
            temp.color("white")
            temp.shape("square")
            temp.bk(i * 20)
            self.list_tut.append(temp)

    def food_eaten(self):
        temp = t.Turtle()
        temp.speed(1)
        temp.penup()
        temp.color("white")
        temp.shape("square")
        last_segment = self.list_tut[-1]
        temp.goto(last_segment.xcor(), last_segment.ycor())
        self.list_tut.append(temp)
        

    def move(self):
        for i in range(len(self.list_tut)-1,0,-1):
            temp1 = self.list_tut[i-1].xcor()
            temp2 = self.list_tut[i-1].ycor()
            self.list_tut[i].goto(x= temp1,y=temp2)

        if self.list_tut[0].xcor() > 300:
            self.list_tut[0].goto(x = -300,y = self.list_tut[0].ycor())
        elif self.list_tut[0].xcor() < -300:
            self.list_tut[0].goto(x = 300,y = self.list_tut[0].ycor())
        elif self.list_tut[0].ycor() > 200:
            self.list_tut[0].goto(x = self.list_tut[0].xcor() ,y = -200)
        elif self.list_tut[0].ycor() < -200:
            self.list_tut[0].goto(x = self.list_tut[0].xcor(),y = 200)
            
            
        self.list_tut[0].forward(20)

    def up(self):
        if self.list_tut[0].heading() != 270:
            self.list_tut[0].setheading(90)

    def down(self):
        if self.list_tut[0].heading() != 90:
            self.list_tut[0].setheading(270)

    def right(self):
        if self.list_tut[0].heading() != 180:
            self.list_tut[0].setheading(0)

    def left(self):
        if self.list_tut[0].heading() != 0:
            self.list_tut[0].setheading(180)