import py5
import time
import sys

filename = sys.argv[0]

num_particles = 2000

inc = 0.1
scl = 40
cols = None
rows = None

zoff = 0

particles = []
flowfield = []

class Particle():
    def __init__(
            self, 
            pos=(0, 0), 
            speed=(0, 0), 
            acc=(0, 0)
        ):
        self.maxspeed = 4
        self.pos   = py5.Py5Vector(pos[0], pos[1])
        self.speed = py5.Py5Vector(speed[0], speed[1])
        self.acc   = py5.Py5Vector(acc[0], acc[1])
        self.prev_pos = self.pos.copy
        self.color = py5.color(py5.random(255), py5.random(255), py5.random(255))

    def update(self):
        self.speed = self.speed + self.acc
        self.speed.set_limit(self.maxspeed)
        self.pos = self.pos + self.speed
        self.acc = self.acc * 0
        
    def apply_force(self, f):
        self.acc +=f
        
    def show(self):
        py5.stroke(self.color, 10)
        py5.stroke_weight(1)
        # py5.point(self.pos.x, self.pos.y)
        py5.line(self.pos.x, self.pos.y, self.prev_pos.x, self.prev_pos.y)
        self.update_prev()
    
    def update_prev(self):
        self.prev_pos.x = self.pos.x
        self.prev_pos.y = self.pos.y
    
    def edges(self):
        if self.pos.x > py5.width:
            self.pos.x = 0
            self.update_prev()
        if self.pos.y > py5.height:
            self.pos.y = 0
            self.update_prev()
        if self.pos.x < 0:
            self.pos.x = py5.width
            self.update_prev()
        if self.pos.y < 0:
            self.pos.y = py5.height
            self.update_prev()
            
    def follow(self, field):
        py5.stroke_weight(1)
        x = py5.floor(self.pos.x/scl)
        y = py5.floor(self.pos.y/scl)
        index = x + y * cols
        # print(index)
        try: # Necessario perchè index spesso è out of bounds
            f = field[index]
            # print("{}, {}".format(index, f))
            self.apply_force(f)
        except Exception as e:
            print(f"{e} -> {index}")
            self.update_prev()
        
def settings():
    py5.size(1280, 800) 


def setup():
    global cols, rows, particles, flowfield, num_particles
    cols = py5.floor(py5.width/scl)
    rows = py5.floor(py5.height/scl)
    for i in range(0, cols*rows):
        flowfield.append(None)
    for i  in range(0, num_particles):
        particles.append(
            Particle(
                pos=(py5.random(py5.width), py5.random(py5.height))
            )
        )
    py5.background(255)
    
    
def draw():
    # py5.background(255)
    global cols, rows, particles, flowfield, zoff, particles, flowfield, inc, scl
    yoff = 0
    for y in range(0, rows):
        xoff = 0
        for x in range(0, cols):
            index = (x + y * cols)
            angle = py5.noise(xoff, yoff, zoff) * py5.PI * 2
            v = py5.Py5Vector.from_heading(angle)
            v.set_mag(0.5)
            flowfield[index] = v
            xoff += inc
            py5.push()
            py5.translate(x * scl, y * scl)
            py5.rotate(v.heading)
            py5.stroke(0)
            # decomment to show vectors
            py5.line(0, 0, 1 * scl, 0)
            py5.pop()
        yoff += inc
    zoff +=0.00004
    for p in particles:
        p.follow(flowfield)
        p.update()
        p.show()
        p.edges()
    
    
def mouse_clicked():
    print(p.get_frame_rate())
    py5.save(f"screenshots/{filename}_{time.time()}.jpg")   
   

py5.run_sketch()