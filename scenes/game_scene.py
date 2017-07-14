import pygame
from scene import Scene

class Game_scene(Scene):

    def get_name(self);
        return ("game")

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


