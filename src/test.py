import tkinter as tk
import numpy as np
import random


class Point:
    def __init__(self, the_canvas, uID):
        self.uID = uID
        self.location = np.ones((2)) * 200
        self.color = "#" + \
            "".join([random.choice('0123456789ABCDEF') for j in range(6)])
        self.the_canvas = the_canvas
        self.the_canvas.create_oval(200, 200, 206, 206,
                                    fill=self.color, outline='', width=0,
                                    tags=('runner'+str(self.uID), 'runner'))

    def move(self):
        delta = (np.random.random((2))-.5)*20

        self.the_canvas.move('runner'+str(self.uID), delta[0], delta[1])


window = tk.Tk()
window.geometry('400x400')
the_canvas = tk.Canvas(window, width=400, height=400, background='black')
the_canvas.grid(row=0, column=0)

points = {}
for i in range(100):
    points[i] = Point(the_canvas, i)


def random_movement():
    for point in points.values():
        point.move()
    window.after(50, random_movement)


random_movement()
window.mainloop()
