import py5 as p
import time
import sys

filename = sys.argv[0]

w, h, r, g, b, x = (0, 0, 0, 0, 0, 0)

# https://www.grc.nasa.gov/www/k-12/airplane/Images/coords.jpg
def cart_polar(x, y):
  return [p.sqrt(x ** 2 + y ** 2), p.atan(y/x) ]

def polar_cart(r, theta):
  return [r * p.cos(theta), r * p.sin(theta)]


def settings():
    p.size(800, 800) 

def setup():
    global r, g, b, w, h
    p.background(0)
    r = p.random(255)
    g = p.random(255)
    b = p.random(255)
    w = p.width
    h = p.height
    # p.frame_rate(1)

def draw():
    global r, g, b, w, h, x
    p.translate(w/2, h/2)
    # p.rotate(x)
    # x+=0.01
    p.stroke_weight(4)
    p.stroke(
       p.remap(p.noise(r), 0, 1, 0, 255),
       p.remap(p.noise(g), 0, 1, 0, 255),
       p.remap(p.noise(b), 0, 1, 0, 255)
    )

    r+=0.01
    g+=0.01
    b+=0.01

    # point = polar_cart(p.frame_count * 0.2, p.frame_count * 0.1)
    # p.point(point[0], point[1])
    if p.frame_count % 6 == 0 :
       point = polar_cart(p.frame_count * 0.2, p.frame_count * 0.1)
       p.point(
          p.remap(point[0], 0, 2000, 0, w),
          p.remap(point[1], 0, 2000, 0, w)
       )

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()