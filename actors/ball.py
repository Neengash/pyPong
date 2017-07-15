import pygame
import random
from actors.actor import Actor

class Ball(Actor):

    width = 10
    height = 10
    base_x_speed = 5
    base_y_speed = 4
    ball_state = {}

    def __init__(self, state):
        self.state = state
        screen_rect = self.state.get_screen().get_rect()
        self.posx = screen_rect.width / 2 - self.width
        self.posy = screen_rect.height / 2 - self.height
        self.velx = 0
        self.vely = 0

    # Just needed for when the ball is not moving and have to
    # start the game.
    def check_inputs(self):
        if self.velx == 0 and self.vely == 0:
            if self.state.get_keys()[pygame.K_SPACE]:
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
        screen = self.state.get_screen()
        pygame.draw.rect(screen, (255, 255, 255), [
            self.posx + self.width / 2,
            self.posy + self.height / 2,
            self.width,
            self.height
        ])

    def check_out_left(self):
        return self.posx + self.width < 0

    def check_out_right(self):
        return self.posx > self.state.get_screen().get_rect().width

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