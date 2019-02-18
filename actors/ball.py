import pygame
from random import randint
from actors.actor import Actor
from drawers.ball_drawer import BallDrawer

class Ball(Actor):

    width = 10
    height = 10
    BASE_SPEED = 5
    drawer = None
    body = None

    def __init__(self, posx, posy, ball_drawer, ball_body):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        self.drawer = ball_drawer
        self.body = ball_body

    def start(self):
        self.velx = randint(-BASE_SPEED, BASE_SPEED)
        self.vely = randint(-BASE_SPEED, BASE_SPEED)

    def update(self):
        self.posx += self.velx
        self.posy += self.vely

    def draw(self):
        self.drawer.draw(
            self.posx, 
            self.posy,
            self.width,
            self.height
        )

    def get_body(self):
        return self.body
