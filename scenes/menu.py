import pygame
from scene import Scene

class Menu(Scene):

    E_START = 0
    E_QUIT = 1

    elements = {
        E_START : 'Start',
        E_QUIT  : 'Quit',
    }

    def __init__(self):
        self.current_element = E_START

    def get_name(self):
        return 'menu'

    def loop(self):
        super().loop()
        #do more things here

    def check_inputs(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
