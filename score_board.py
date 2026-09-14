from turtle import Turtle
FONT=("Courier", 27, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        file.close()
        self.color("white")
        self.penup()
        self.goto(0, 330)
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center",font=FONT)
        self.hideturtle()


    def score_increase(self):
        self.score+=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center",font=FONT )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
