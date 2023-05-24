import py5 as p
import time
import sys

filename = sys.argv[0]

def to_degrees(a):
    return a * 180 / p.PI


center_x = 400
center_y = 400
radius = 100     
eye = None

eyes_list = []

eyes_num = 8


class Eye:
    def __init__(self, x, y, d, d2):
        self.center = p.Py5Vector2D(x, y)
        self.center_2 = p.Py5Vector2D.random()
        self.diameter = d
        self.diameter_2 = d2
        self.debug = False


    def draw(self):
        p.fill(255)
        p.circle(self.center.x, self.center.y, self.diameter)
        v2 = p.Py5Vector2D(p.mouse_x, p.mouse_y)
        center_2 = v2 - self.center
        center_2.set_limit(self.diameter / 2 - self.diameter_2 / 2)
        if self.debug:
            p.line(
                self.center.x, 
                self.center.y, 
                self.center.x + center_2.x, 
                self.center.y + center_2.y
            )

        p.fill(0)
        p.circle(
            self.center.x + center_2.x, 
            self.center.y + center_2.y,
            self.diameter_2
        )


def settings():
    p.size(800, 800) 

def setup():
    global eye, eyes_list, eyes_num
    # eye = Eye(400, 400, 100, 20)
    d = p.width / eyes_num
    for i in range(0, eyes_num):
        for j in range(0, eyes_num):
            eyes_list.append(Eye(
                i * d + d/2, j * d + d/2, d, d/4
            ))
        

    pass
    # p.frame_rate(1)

def draw():
    p.background(200)
    global v, center_x, center_y, radius, eye
    '''
    v1 = p.Py5Vector2D(center_x, center_y)
    v2 = p.Py5Vector2D(p.mouse_x, p.mouse_y)
    v3 = v2 - v1

    v3.set_limit(radius)

    p.stroke(0, 0, 255)
    p.line(0, 0, v1.x, v1.y)
    p.stroke(0, 255, 255)
    p.line(0, 0, v2.x, v2.y)
    p.stroke(255, 255, 255)
    p.line(v1.x, v1.y, v1.x + v3.x, v1.y + v3.y)
    print("")
    print(v1.x, v1.y)
    print(v2.x, v2.y)
    print(v3.x, v3.y)
    

    '''
    
    # eye.draw()

    for eye in eyes_list:
        eye.draw()

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   




p.run_sketch()