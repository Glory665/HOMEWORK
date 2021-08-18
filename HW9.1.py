import turtle
from time import sleep

t = turtle.Turtle()

class TrafficLight:


    def __init__(self, r, g, gr):
        self.red = r
        self.gold = g
        self.green = gr


    def running(self):
        while True:
            t.shape('turtle')
            t.color(self.red)
            sleep(7)
            t.shape('turtle')
            t.color(self.gold)
            sleep(2)
            t.shape('turtle')
            t.color(self.green)
            sleep(5)


trafficlight = TrafficLight("red", "gold", "green")
trafficlight.running()

