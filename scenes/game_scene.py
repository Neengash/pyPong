import pygame
from scenes.scene import Scene
from actors.bar import Bar
from actors.ball import Ball
from engine import Engine

class Game_scene(Scene):

    M_1player  = 1
    M_2players = 2

    def __init__(self, state, mode):
        self.mode = mode
        self.actors = self.get_actors_for_mode(state)
        self.pause = False
        self.win = False
        self.score = [0, 0]

    # When more modes are allowed, this should be changed
    def get_actors_for_mode(self, state):
        return [
            Bar(state, 1),
            Bar(state, 2),
            #Ball(state),
        ]

    def loop_step(self, state):
        self.check_inputs(state)
        self.update(state)
        self.draw(state)

    def check_inputs(self, state):
        for actor in self.actors:
            actor.check_inputs(state)

    def update(self, state):
        for actor in self.actors:
            actor.update(state)

    def draw(self, state):
        self.draw_scenario()
        for actor in self.actors:
            actor.draw(state)

    def draw_scenario(self):
        pass