from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.score()
    
    # Scoreboard
    def score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increase the score
    def next(self):
        self.level += 1
        self.clear()
        self.score()

    # Game Over 
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
