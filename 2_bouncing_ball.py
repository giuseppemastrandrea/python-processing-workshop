import py5 as p
import time
import sys

filename = sys.argv[0]

x = 200
y = 200
d = 50
dx = 2
dy = 3


def settings():
    p.size(800, 800) 

def setup():
    pass
    # p.frame_rate(1)

def draw():
    global x, y, d, dx, dy
    p.background(255, 0, 0)
    p.circle(x, y, d)

    x = x + dx
    y = y + dy

    if x > (p.width - d/2) or x < d/2:
        dx = -dx

    if y > (p.height - d/2) or y < d/2:
        dy = -dy

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()