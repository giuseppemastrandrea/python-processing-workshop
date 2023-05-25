import py5 as p
import time
import sys

filename = sys.argv[0]

startX, startY, side = (0, 0, 20)

def settings():
    p.size(800, 800) 

def setup():
    pass
    # p.frame_rate(1)

def draw():
    global startX, startY, side
    if p.random() < 0.5:
        p.line(startX, startY, startX + side, startY + side)
    else:
        p.line(startX, startY + side, startX + side, startY)
    
    startX += side

    if startX > p.width:
        startX = 0
        startY += side

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()