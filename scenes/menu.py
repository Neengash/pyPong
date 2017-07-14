import pygame
from scenes.scene import Scene

class Menu(Scene):

    E_START = 0
    E_QUIT = 1

    elem_labels = {
        E_START : 'Start',
        E_QUIT  : 'Quit',
    }

    def __init__(self):
        self.current_element = Menu.E_START
        self.font = pygame.font.Font("foo_font.ttf", 36)

    def loop_step(self, state):
        super().loop(state)
        #do more things here

    def check_inputs(self, state):
        pass

    def update(self, state):
        pass

    def draw(self, state):
        screen = state.get_screen()
        text1 = self.font.render("Hello", 1, (255, 255, 255))
        textpos = text1.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text1, textpos)
