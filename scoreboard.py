from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", "24", "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()
        

    def update_score(self):
        if self.score > 0:
            self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)