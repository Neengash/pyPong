import pygame
import datetime
from scenes.scene import Scene

class Menu(Scene):

    E_START = 0
    E_QUIT = 1

    menu_options = {
        E_START : 'Start',
        E_QUIT  : 'Quit',
    }

    def __init__(self):
        self.current_element = Menu.E_START
        self.font = pygame.font.Font("foo_font.ttf", 36)
        self.last_update = None

    def loop_step(self, state):
        super().loop(state)
        #do more things here

    def check_inputs(self, state):
        if state.keys[pygame.K_DOWN]:
            self.switch_current_element()

    def switch_current_element(self):
        if self.last_update == None:
            self.last_update = datetime.datetime.now()
        else:
            now = datetime.datetime.now()
            diference = now - self.last_update
            if diference.microseconds < 250000:
                return None
            self.last_update = now

        if self.current_element == Menu.E_START:
            self.current_element = Menu.E_QUIT
        else:
            self.current_element = Menu.E_START

    def update(self, state):
        pass

    def draw(self, state):
        screen = state.get_screen()
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