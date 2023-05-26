import py5 as p
import time
import sys

filename = sys.argv[0]


x = None
y = None
d = 50
start = 0


def settings():
    p.size(800, 800) 

def setup():
    global start, x, y
    s = p.noise(start)
    x = p.remap(s, 0, 1, 0, p.width)
    y = p.remap(s, 0, 1, 0, p.height)
    # p.frame_rate(1)

def draw():
    global x, y, d, start
    p.no_stroke()
    p.fill(0, 7)
    p.rect(0, 0, p.width, p.height)

    p.fill(255, 0, 0)
    p.circle(x, y, d)
    start = start + 0.01
    s = p.noise(start)
    x = p.remap(s, 0, 1, 0, p.width)

    p2 = p.noise(start + 100)
    y = p.remap(p2, 0, 1, 0, p.height)
    

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()