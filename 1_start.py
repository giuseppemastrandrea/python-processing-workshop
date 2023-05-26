import py5 as p
import time
import sys

filename = sys.argv[0]

x = 200
y = 400
d = 50

def settings():
    p.size(800, 800) 

def setup():
    pass
    # p.frame_rate(1)

def draw():
    global x, y, d
    p.background(255, 0, 0)
    p.circle(x, y, d)
    x = x + 3
    if x > (p.width + d/2):
        x = - d/2
    if x < -d/2:
        x = p.width + d/2
    
    y = y - 4 
    if y > (p.height + d/2):
        y = - d/2
    if y < 0:
        y = p.height + d/2
    

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()