import pygame
from actors.actor import Actor
from drawers.bar_drawer import BarDrawer

class Bar(Actor):

    speed = 5
    width = 10
    height = 50
    drawer = None
    body = None

    def __init__(self, posx, posy, bar_drawer, bar_body):
        self.posx = posx
        self.posy = posy
        self.vely = 0
        self.accy = 0
        self.drawer = bar_drawer
        self.body = bar_body

    def update(self):
        self.vely += self.accy
        self.posy += self.vely

    def draw(self):
        self.drawer.draw(
            self.posx, 
            self.posy,
            self.width,
            self.height
        )
