import py5 as p
import time
import sys

filename = sys.argv[0]

x, y, dx, dy, d = (0, 0, +2, -4, 50)

ball = None

class Ball:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.dx = p.random(-5, 5)
        self.dy = p.random(-5, 5)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.edges()
        p.circle(self.x, self.y, self.d)

    def edges(self):
        if self.x > p.width or self.x < 0:
            self.dx = -self.dx

        if self.y > p.height or self.y < 0:
            self.dy = -self.dy


def settings():
    p.size(800, 800) 

def setup():
    global ball
    ball = Ball(p.random(800), p.random(800), 50)
    # p.frame_rate(1)

def draw():
    global ball
    ball.move()
    

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   

p.run_sketch()