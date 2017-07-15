import pygame
from scenes.scene import Scene
from actors.bar import Bar
from actors.ball import Ball
from engine import Engine

class Game_scene(Scene):

    M_1player  = 1
    M_2players = 2

    mode = None
    actors = []
    pause = None

    def __init__(self, mode):
        self.mode = mode
        self.actors = [
            Bar(),
            Bar(),
            Ball(),
        ]
        self.pause = False

    def loop_step(self, state):
        self.check_inputs(state)
        self.update(state)
        self.draw(state)

    def check_inputs(self, state):
        pass

    def update(self, state):
        pass

    def draw(self, state):
        screen = state.get_screen()
        pygame.draw.rect(screen, (255, 255, 255), [75, 10, 50, 20], 2)
