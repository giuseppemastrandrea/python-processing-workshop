import py5 as p
import time
import sys

filename = sys.argv[0]

balls = []
ballsNum = 5


class Swarm:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        self.off1 = p.random(100)
        self.off2 = p.random(100)

        self.inc = 0.01

    def move(self):
        self.x = p.noise(self.off1) * p.width
        self.y = p.noise(self.off2) * p.height
        p.no_stroke()
        p.fill(self.color)
        p.circle(self.x, self.y, self.radius)
        self.off1 += self.inc
        self.off2 += self.inc


def settings():
    p.size(800, 800) 

def setup():
    global balls, ballsNum
    for i in range(0, ballsNum):
        balls.append(Swarm(p.width, p.height, 20, p.color(255, 158, 158)))
    # p.frame_rate(1)

def draw():
    p.fill(0, 10)
    p.rect(0, 0, p.width, p.height)
    global balls
    for b in balls:
        b.move()

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()