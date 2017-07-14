import pygame
import scene

class Menu(Scene):

    selected_element = 0

    elements = [
        'Start'
        'Quit'
    ]

    def loop(self):
        self.check_inputs()
        self.update()
        self.draw()

    def check_inputs(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


