import pygame
import random
from actors.actor import Actor
from drawers.ball_drawer import BallDrawer
from actors.bar import Bar

class Ball(Actor):

    width = 10
    height = 10
    base_x_speed = 5
    base_y_speed = 4
    ball_state = {}

    def __init__(self, posx, posy, ball_drawer):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        self.drawer = ball_drawer

    # Just needed for when the ball is not moving and have to
    # start the game.
    def check_inputs(self, keys):
        if self.velx == 0 and self.vely == 0:
            if keys[pygame.K_SPACE]:
                self.velx = 5

    def update(self):
        #pending to check for min and max speeds
        self.posx += self.velx
        self.posy += self.vely

        screen_height = self.state.get_screen().get_rect().height
        if self.posy < 0:
            self.posy = 1/2 * self.height
            self.vely = - self.vely
        elif self.posy > screen_height - self.height:
            self.posy = screen_height - self.height
            self.vely = - self.vely

    def draw(self):
        self.drawer.draw(
            self.posx, 
            self.posy,
            self.width,
            self.height
        )

    def check_out_left(self):
        return self.posx + self.width < 0

    def check_out_right(self):
        return self.posx > (self.state.get_screen().get_rect().width + self.width)

    def set_ball_for_player(self, player):
        if player == 1:
            self.posx = 30
            self.posy = self.state.get_screen().get_rect().height / 2
            self.velx = 5
            self.vely = random.randint(-self.base_y_speed, self.base_y_speed)
        else:
            self.posx = self.state.get_screen().get_rect().width - 30 - self.width
            self.posy = self.state.get_screen().get_rect().height / 2
            self.velx = -5
            self.vely = random.randint(-self.base_y_speed, self.base_y_speed)

    def check_and_resolve_collisions(self, actors):
        for actor in actors:
            if isinstance(actor, Bar):
                if self.check_collision(actor):
                    self.resolve_collision(actor)

    def check_collision(self, actor):
        return (
            self.posx + self.width > actor.posx and
            self.posx < actor.posx + actor.width and
            self.posy + self.height > actor.posy and
            self.posy < actor.posy + actor.height
        )

    def resolve_collision(self, actor):
        if self.velx > 0:
            self.posx = actor.posx - self.width
            self.velx = -self.velx + random.randint(-1, 1)
            self.vely += random.randint(-2, 2)
        else:
            self.posx = actor.posx + actor.width
            self.velx = -self.velx + random.randint(-1, 1)
            self.vely += random.randint(-2, 2)
