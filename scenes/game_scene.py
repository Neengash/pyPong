import pygame
from scenes.scene import Scene

class Game_scene(Scene):

    def loop_step(self):
        self.check_inputs()
        self.update()
        self.draw()

    def check_inputs(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


