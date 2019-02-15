import pygame
from actors.actor import Actor

class Bar(Actor):

    speed = 5
    width = 10
    height = 50
    bar_state = {}

    def __init__(self, state, player):
        self.state = state
        screen_rect = self.state.get_screen().get_rect()
        self.posx = self.get_player_posx(screen_rect, player)
        self.posy = (screen_rect.bottom / 2) - self.width / 2
        self.reset_bar_state()
        self.set_movement_keys(player)

    def get_player_posx(self, screen_rect, player):
        if player == 1:
            return screen_rect.left + self.width / 2
        elif player == 2:
            return screen_rect.right - self.width * 3 / 2

    def set_movement_keys(self, player):
        if player == 1:
            self.key_up = pygame.K_q
            self.key_down = pygame.K_a
        elif player == 2:
            self.key_up = pygame.K_p
            self.key_down = pygame.K_l

    def reset_bar_state(self):
        self.bar_state = {
            'up'   : False,
            'down' : False,
        }

    def check_inputs(self):
        self.reset_bar_state()
        if self.check_go_up():
            self.bar_state['up'] = True
        if self.check_go_down():
            self.bar_state['down'] = True

    def check_go_up(self):
        return (
            self.state.get_keys()[self.key_up] and
            self.posy > 0
        )

    def check_go_down(self):
        return (
            self.state.get_keys()[self.key_down] and
            self.posy < self.state.get_screen().get_rect().height - self.height
        )

    def update(self):
        if self.bar_state['up']:
            self.posy -= Bar.speed
        if self.bar_state['down']:
            self.posy += Bar.speed

    def draw(self):
        screen = self.state.get_screen()
        pygame.draw.rect(screen, (255, 255, 255),
            [self.posx, self.posy, self.width, self.height])
