import py5 as p
import time
import sys

filename = sys.argv[0]

lato = 40
startX = 0
startY = 0

def settings():
    p.size(800, 800) 

def setup():
    # p.frame_rate(3)
    p.background(0)
    pass
    

def draw():
    
    p.stroke(255)
    global startX, startY, lato
    r = p.random()
    if r > 0.8:
        p.line(startX, startY, startX + lato, startY + lato)
    else:
        p.line(startX, startY + lato , startX + lato, startY)

    startX = startX + lato

    if startX >= p.width:
        startY = startY + lato
        startX = 0
    
    if startY >= p.height:
        # p.background(0)
        # startX = 0
        # startY = 0
        p.save(f"screenshots/{filename}_{time.time()}.jpg")   
        p.no_loop()
    

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()