import py5 as p
import time
import sys

filename = sys.argv[0]


balls = []
NUM_BALLS = 50


class Ball:
    def __init__(self, x, y, d, dx, dy):
        self.x = x
        self.y = y
        self.d = d
        self.dx = dx
        self.dy = dy 
        self.color = p.color(
            p.random(255),
            p.random(255),
            p.random(255)
        )

    def move(self):
        p.no_stroke()
        p.fill(self.color)
        p.circle(self.x, self.y, self.d)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.edges()

    def edges(self):
        if self.x > (p.width - self.d/2) or self.x < self.d/2:
            self.dx = -self.dx

        if self.y > (p.height - self.d/2) or self.y < self.d/2:
            self.dy = -self.dy


def settings():
    p.size(800, 800) 

def setup():
    global balls, NUM_BALLS
    for i in range(NUM_BALLS):
        balls.append(
            Ball(
                p.random(p.width),
                p.random(p.height),
                p.random(30, 60),
                p.random(-5, 5),
                p.random(-5, 5)
            )
        )
    # p.frame_rate(1)

def draw():
    global balls
    p.background(0)
    for b in balls:
        b.move()
    

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()