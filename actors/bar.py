import pygame
from actors.actor import Actor

class Bar(Actor):

    speed = 5
    width = 10
    height = 50
    bar_state = {}

    def __init__(self, state, player):
        screen_rect = state.get_screen().get_rect()
        self.posx = screen_rect.left + self.width / 2
        self.posy = screen_rect.top / 2
        self.reset_bar_state()

    def reset_bar_state(self):
        self.bar_state = {
            'up'   : False,
            'down' : False,
        }

    def check_inputs(self, state):
        self.reset_bar_state()
        if state.get_keys()[pygame.K_q]:
            self.bar_state['up'] = True
        if state.get_keys()[pygame.K_a]:
            self.bar_state['down'] = True

    def update(self, state):
        if self.bar_state['up']:
            self.posy -= Bar.speed
        if self.bar_state['down']:
            self.posy += Bar.speed

    def draw(self, state):
        screen = state.get_screen()
        pygame.draw.rect(screen, (255, 255, 255),
            [self.posx, self.posy, self.width, self.height])
