import py5 as p
import time
import sys

filename = sys.argv[0]


def settings():
    p.size(800, 800) 

def setup():
    pass
    # p.frame_rate(1)

def draw():
    p.background(200)
    v1 = p.Py5Vector(200, 200)
    v2 = p.Py5Vector(p.mouse_x, p.mouse_y)
    diff = v2 - v1
    sum = v1 + v2

    p.stroke(255, 0, 0)
    p.line(0, 0, v1.x, v1.y)
    p.stroke(0, 255, 0)
    p.line(0, 0, v2.x, v2.y)
    p.stroke(0, 0, 255)
    p.line(0, 0, sum.x, sum.y)
    p.stroke(255, 255, 0)
    p.line(v1.x, v1.y, v1.x + diff.x, v1.y + diff.y)

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()