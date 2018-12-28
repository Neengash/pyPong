import pygame
import datetime
from scenes.scene import Scene

class Menu(Scene):

    E_START = 0
    E_QUIT = 1

    TIME_TO_REACTIVATE = 250000

    menu_options = {
        E_START : 'Start',
        E_QUIT  : 'Quit',
    }

    menu_state = {
        'up'   : False,
        'down' : False,
        'action' : False,
    }

    def __init__(self, state):
        self.state = state
        self.current_element = Menu.E_START
        self.font = pygame.font.Font("foo_font.ttf", 36)
        self.last_update = None
        self.clean_state() #menu_state

    def loop_step(self):
        self.clean_state()
        super().loop()

    def clean_state(self):
        self.menu_state = {
            'up'   : False,
            'down' : False,
            'action' : False,
        }

    def check_inputs(self):
        for event in self.state.get_loop_events():
            if self.check_key(event, pygame.K_DOWN):
                self.menu_state['down'] = True
                self.last_update = datetime.datetime.now()
            elif self.check_key(event, pygame.K_UP):
                self.menu_state['up'] = True
                self.last_update = datetime.datetime.now()
            elif self.check_key(event, pygame.K_RETURN):
                self.menu_state['action'] = True

        if not any(list(self.menu_state.values())):
            now = datetime.datetime.now()
            if self.state.keys[pygame.K_DOWN] and self.time_to_reactivate(now):
                self.menu_state['down'] = True
            elif self.state.keys[pygame.K_UP] and self.time_to_reactivate(now):
                self.menu_state['up'] = True

    def check_key(self, event, key):
        return event.type == pygame.KEYDOWN and event.key == key

    def time_to_reactivate(self, now):
        if not self.last_update:
            self.last_update = now
            return false

        if (now - self.last_update) >= self.TIME_TO_REACTIVATE:
            self.last_update = now
            return True
        return False

    def update(self):
        if self.menu_state['action']:
            if self.current_element == Menu.E_START:
                self.state.start_game()
            elif self.current_element == Menu.E_QUIT:
                self.state.stop_running()
        elif self.menu_state['down']:
            new_elem = self.current_element + 1
            if new_elem not in self.menu_options:
                new_elem = list(self.menu_options)[0]
            self.current_element = new_elem
        elif self.menu_state['up']:
            new_elem = self.current_element - 1
            if new_elem not in self.menu_options:
                new_elem = list(self.menu_options)[-1]
            self.current_element = new_elem

    def draw(self):
        screen = self.state.get_screen()
        x_center = screen.get_rect().centerx
        y_center = screen.get_rect().centery
        for key, menu_option in self.menu_options.items():
            if key == self.current_element:
                text = self.font.render(
                    menu_option, 1, (0, 0, 0), (255, 255, 255)
                )
            else:
                text = self.font.render(
                    menu_option, 1, (255, 255, 255)
                )
            pos = text.get_rect()
            pos.centerx = x_center
            pos.centery = y_center
            if key % 2 == 0:
                pos.centery -= 50
            else :
                pos.centery += 50
            screen.blit(text, pos)
