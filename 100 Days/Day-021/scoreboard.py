from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("100 Days\Day-021\data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        
        if self.score > self.highscore:
            self.highscore = self.score
            with open("100 Days\Day-021\data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.update_score()
