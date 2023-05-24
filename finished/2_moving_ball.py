import py5 as p
import time
import sys

filename = sys.argv[0]

x, y, dx, dy, d = (0, 0, +2, -4, 50)
def settings():
    p.size(800, 800) 

def setup():
    pass
    # p.frame_rate(1)

def draw():
    global x, y, dx, dy, d
    x += dx
    y += dy

    if x > p.width or x < 0:
        dx = -dx

    if y > p.height or y < 0:
        dy = -dy
    p.circle(x, y, d)
    

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   

p.run_sketch()