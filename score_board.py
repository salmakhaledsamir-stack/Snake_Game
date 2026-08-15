from turtle import Turtle
FONT=("Courier", 27, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align="center",font=FONT)
        self.hideturtle()


    def score_increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center",font=FONT )


    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("Game Over.", False, align="center", font=("Courier", 30, "bold"))
