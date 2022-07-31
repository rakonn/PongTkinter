import tkinter as tk
import keyboard as kbd
import time
import math

# note() : create space dash for paddle movement
# note() : enable respawn functionality


class PongGame():
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.canvas = tk.Canvas(root, bg="#1d1d1f", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.start = 0

        self.leftPaddle = Paddle(70, 200, 80, 300, self.canvas)
        self.rightPaddle = Paddle(840, 200, 830, 300, self.canvas)
        self.ball = Ball(445, 245, 455, 255, self.canvas)
        self.run()

    def run(self):
        self.update()

    def update(self):
        # end = time.time()
        # deltaTime = end - self.start
        # print(deltaTime)

        if kbd.is_pressed("w"):
            self.leftPaddle.moveUp()
        if kbd.is_pressed("s"):
            self.leftPaddle.moveDown()

        if kbd.is_pressed("up"):
            self.rightPaddle.moveUp()
        if kbd.is_pressed("down"):
            self.rightPaddle.moveDown()
        # if kbd.is_pressed("a"):
        #     self.leftPaddle.moveLeft()
        # if kbd.is_pressed("d"):
        #     self.leftPaddle.moveRight()

        # self.start = time.time()
        self.ball.update()

        self.canvas.after(15, lambda: self.update())


class Paddle():
    sizeStep = 3

    def __init__(self, x0: float, y0: float, x1: float, y1: float, canvas: tk.Canvas) -> None:
        self.canvas = canvas
        self.rect = canvas.create_rectangle(
            x0, y0, x1, y1, fill="#ffffff", width=0)

    def moveDown(self):
        if self.canvas.coords(self.rect)[3] < 500:
            self.canvas.move(self.rect, 0, self.sizeStep)

    def moveUp(self):
        if self.canvas.coords(self.rect)[1] >= 0:
            self.canvas.move(self.rect, 0, -self.sizeStep)

    # def moveLeft(self):
    #     self.canvas.move(self.rect, -self.sizeStep, 0)

    # def moveRight(self):
    #     self.canvas.move(self.rect, self.sizeStep, 0)


class Ball():
    def __init__(self, x0: float, y0: float, x1: float, y1: float, canvas: tk.Canvas) -> None:
        self.canvas = canvas
        self.ball = canvas.create_oval(
            x0, y0, x1, y1, fill="#ffffff", width=0, outline="")
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.speed = 2
        self.direction = 167

    def update(self):
        coords = self.canvas.coords(self.ball)

        if coords[0] <= 0:
            #needs goal behaviour
            self.direction = 180 - self.direction
            print("goal left")
        elif coords[0] >= 895:            
            #needs goal behaviour
            self.direction = 180 - self.direction
            print("goal right")
        elif coords[1] <= 0:
            self.direction = 360 - self.direction
        elif coords[1] >= 495:
            self.direction = 360 - self.direction
        elif len(self.canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])) > 1:
            self.direction = 180 - self.direction

        xComponent = round(6 * math.cos(self.direction * (math.pi / 180)))
        yComponent = round(6 * math.sin(self.direction * (math.pi / 180)))

        self.canvas.move(self.ball, xComponent, yComponent)


root = tk.Tk()
root.geometry("900x500")

PongGame(root)

root.mainloop()
