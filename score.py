from turtle import Turtle

ALLIGN="center"
FONT=("Arial",12,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.score=0
        self.write(f"Score: {self.score}",align="center",font=("Arial",12,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over !",align="center",font=("Arial",24,"normal"))


    def update_score(self):
        self.write(f"Score: {self.score}",align=ALLIGN,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
        

