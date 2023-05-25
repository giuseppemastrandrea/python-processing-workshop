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
    p.background(1, 75, 100);
    p.fill(237, 34, 93)
    p.no_stroke()
    d = 50
    for i in range(int(p.width / d)):
        for j in range(int(p.height / d)):
            p.ellipse(
                d/2 + i * d,
                d/2 + j * d,
                d*p.noise(p.frame_count/100 + j*10000 + i*10000),
                d*p.noise(p.frame_count/100 + j*10000 + i*10000)
            )

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()