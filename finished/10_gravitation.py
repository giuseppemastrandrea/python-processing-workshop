import py5 as p
import time
import sys

filename = sys.argv[0]


movers = []

class Mover:
  def __init__(self, accX, accY):
    self.location = p.Py5Vector(
      p.random(p.width),
      p.random(p.height)
    )
    self.speed = p.Py5Vector(0, 0)
    self.diameter = p.random(10, 20)
    self.acceleration = p.Py5Vector(accX, accY)
    self.maxSpeed = 6
    self.r = p.random(255)
    self.g = p.random(255)
    self.b = p.random(255)
  
  
  def move(self):
    self.updatePosition()
    # self.checkEdges()
    self.draw()
  
  
  def limitSpeed(self):
    if self.speed.mag > self.maxSpeed:
      print("Limiting Speed!")
      self.speed.normalize()
      self.speed *= self.maxSpeed
    
  
  
  def updateAcceleration(self, v):
    self.acceleration = v
  
  
  def updatePosition(self):
    self.speed += self.acceleration
    self.limitSpeed()
    self.location += self.speed
  
  
  def checkEdges(self):
    if self.location.x <= 0:
        self.location.x = p.width
    elif self.location.x >= p.width:
        self.location.x = 0
    
    
    if self.location.y <= 0:
        self.location.y = p.width
    elif self.location.y >= p.height:
        self.location.y = 0
    
  
  
  def draw(self):
    p.no_stroke()
    p.fill(self.r, self.g, self.b)
    p.circle(self.location.x, self.location.y, self.diameter)
  


def settings():
    p.size(800, 800) 

def setup():
    global movers
    for i in range(50):
       movers.append(Mover(0.01, 0.005))
    # p.frame_rate(1)

def draw():
    p.fill(0, 10)
    p.rect(0, 0, p.width, p.height)
    global movers
    mouse = p.Py5Vector(p.mouse_x, p.mouse_y)
    for mover in movers:
        diff = mouse - mover.location
        diff.normalize()
        diff = diff * 0.05
        p.stroke(255)
        mover.updateAcceleration(diff)
        mover.move()

def mouse_clicked():
    print(p.get_frame_rate())
    p.save(f"screenshots/{filename}_{time.time()}.jpg")   



p.run_sketch()