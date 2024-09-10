import turtle as t



class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = file.read()
        self.penup()
        self.hideturtle()
        self.goto(0,160)
        self.score = 0
        self.color("#f1e0c5")
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score}",align="center",font = ("Arial",25,"bold"))
        
    def update(self): 
        self.hideturtle()
        self.score += 1
        self.clear()
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score}",align="center",font = ("Arial",25,"bold"))
        if self.score >= int(self.high_score):
            self.high_score = self.score+1
            with open("high_score.txt",mode = "w") as file:
                file.write(str(self.score))



