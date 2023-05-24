import py5 as p
import time
import sys

filename = sys.argv[0]

d = 100
r = d/2

def draw_hexagon(x, y, d, color):
  r = d/2
  # p.circle(x, y, d)
  p.fill(color)
  p.begin_closed_shape()
  p.vertex(x + r, y)
  p.vertex(x + r / 2, y + p.sqrt(3)/2 * r)
  p.vertex(x - r / 2, y + p.sqrt(3)/2 * r)
  p.vertex(x - r, y)
  p.vertex(x - r / 2, y - p.sqrt(3)/2 * r)
  p.vertex(x + r / 2, y - p.sqrt(3)/2 * r)
  p.end_shape(p.CLOSE)


def draw_nested_hexagon(x, y, d):
  # circle(x, y, d)
  draw_hexagon(x, y, d, "#8D5A97")
  draw_hexagon(x, y, .875*d, "#907F9F")
  draw_hexagon(x, y, .750*d, "#A4A5AE")
  draw_hexagon(x, y, .625*d, "#B0C7BD")
  draw_hexagon(x, y, .500*d, "#B8EBD0")
  draw_hexagon(x, y, .375*d, "#BEEDD4")
  draw_hexagon(x, y, .250*d, "#C4EFD8")
  draw_hexagon(x, y, .125*d, "#C9F0DC")


def settings():
    p.size(400, 400 - int(p.sqrt(3)/2))


def setup():
    p.background(255)
    
    
def draw():
    global d, r
    p.background(220);
    yDist = p.sqrt(3)*r # Altezza totale dell'esagono, ci serve per calcolare dove disegnare gli altri esagoni. Ad esempio se l'altezza dell'esagono è 40
    

    draw_nested_hexagon(50 - r*1.5, 50 - 1*yDist/2, d)
    draw_nested_hexagon(50 - r*1.5, 50 + 1*yDist/2, d)
    draw_nested_hexagon(50 - r*1.5, 50 + 3*yDist/2, d)
    draw_nested_hexagon(50 - r*1.5, 50 + 5*yDist/2, d)
    draw_nested_hexagon(50 - r*1.5, 50 + 7*yDist/2, d)

    draw_nested_hexagon(50, 50 - 1*yDist, d) # 50, 10
    draw_nested_hexagon(50, 50 + 0*yDist, d) # 50, 50
    draw_nested_hexagon(50, 50 + 1*yDist, d) # 50, 90
    draw_nested_hexagon(50, 50 + 2*yDist, d) # 50, 130
    draw_nested_hexagon(50, 50 + 3*yDist, d) # 50, 170
    draw_nested_hexagon(50, 50 + 4*yDist, d)
    draw_nested_hexagon(50, 50 + 5*yDist, d)
    
    draw_nested_hexagon(50 + r*1.5, 50 - 1*yDist/2, d)
    draw_nested_hexagon(50 + r*1.5, 50 + 1*yDist/2, d)
    draw_nested_hexagon(50 + r*1.5, 50 + 3*yDist/2, d)
    draw_nested_hexagon(50 + r*1.5, 50 + 5*yDist/2, d)
    draw_nested_hexagon(50 + r*1.5, 50 + 7*yDist/2, d)
    draw_nested_hexagon(50 + r*1.5, 50 + 9*yDist/2, d)
    
    draw_nested_hexagon(50 + 3*r, 50 - 1*yDist, d)
    draw_nested_hexagon(50 + 3*r, 50 + 0*yDist, d)
    draw_nested_hexagon(50 + 3*r, 50 + 1*yDist, d)
    draw_nested_hexagon(50 + 3*r, 50 + 2*yDist, d)
    draw_nested_hexagon(50 + 3*r, 50 + 3*yDist, d)
    draw_nested_hexagon(50 + 3*r, 50 + 4*yDist, d)
    draw_nested_hexagon(50 + 3*r, 50 + 5*yDist, d)
    
    draw_nested_hexagon(50 + r*4.5, 50 - 1*yDist/2, d)
    draw_nested_hexagon(50 + r*4.5, 50 + 1*yDist/2, d)
    draw_nested_hexagon(50 + r*4.5, 50 + 3*yDist/2, d)
    draw_nested_hexagon(50 + r*4.5, 50 + 5*yDist/2, d)
    draw_nested_hexagon(50 + r*4.5, 50 + 7*yDist/2, d)
    draw_nested_hexagon(50 + r*4.5, 50 + 9*yDist/2, d)
    
    draw_nested_hexagon(50 + 6*r, 50 - 1*yDist, d)
    draw_nested_hexagon(50 + 6*r, 50 + 0*yDist, d)
    draw_nested_hexagon(50 + 6*r, 50 + 1*yDist, d)
    draw_nested_hexagon(50 + 6*r, 50 + 2*yDist, d)
    draw_nested_hexagon(50 + 6*r, 50 + 3*yDist, d)
    draw_nested_hexagon(50 + 6*r, 50 + 4*yDist, d)
    draw_nested_hexagon(50 + 6*r, 50 + 5*yDist, d)
    
    draw_nested_hexagon(50 + r*7.5, 50 - 1*yDist/2, d)
    draw_nested_hexagon(50 + r*7.5, 50 + 1*yDist/2, d)
    draw_nested_hexagon(50 + r*7.5, 50 + 3*yDist/2, d)
    draw_nested_hexagon(50 + r*7.5, 50 + 5*yDist/2, d)
    draw_nested_hexagon(50 + r*7.5, 50 + 7*yDist/2, d)
    
def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   


p.run_sketch()