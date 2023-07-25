from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("data.txt", mode="r")
        self.high_score = int(file.read())
        file.close()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", mode="w")
            file.write(f"{self.high_score}")
            file.close()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

