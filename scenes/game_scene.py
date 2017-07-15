import pygame
from scenes.scene import Scene
from actors.bar import Bar
from actors.ball import Ball
from engine import Engine

class Game_scene(Scene):

    M_1player  = 1
    M_2players = 2

    def __init__(self, state, mode):
        self.state = state
        self.mode = mode
        self.actors = self.get_actors_for_mode()
        self.pause = False
        self.win = False
        self.score = [0, 0]

    # When more modes are allowed, this should be changed
    def get_actors_for_mode(self):
        return [
            Bar(self.state, 1),
            Bar(self.state, 2),
            Ball(self.state),
        ]

    def loop_step(self):
        self.check_inputs()
        self.update()
        self.draw()

    def check_inputs(self):
        for actor in self.actors:
            actor.check_inputs()

    def update(self):
        for actor in self.actors:
            actor.update()

            if isinstance(actor, Ball):
                if actor.check_out_left():
                    self.p2_score()
                    self.actors.remove(actor)
                    if not self.win:
                        self.new_p1_ball()
                elif actor.check_out_right():
                    self.p1_score()
                    self.actors.remove(actor)
                    if not self.win:
                        self.new_p2_ball()

    def p1_score(self):
        self.scores[0] += 1
        if self.scores[0] == 9:
            self.raise_win(1)

    def p2_score(self):
        self.scores[1] += 1
        if self.scores[1] == 9:
            self.raise_win(2)

    def raise_win(player):
        pass

    def new_p1_ball(self):
        pass

    def new_p2_ball(self):
        pass

    def draw(self):
        self.draw_scenario()
        for actor in self.actors:
            actor.draw()

    def draw_scenario(self):
        screen = self.state.get_screen()
        pygame.draw.line(screen, (255, 255, 255),
            (screen.get_rect().width / 2, 0),
            (screen.get_rect().width / 2, screen.get_rect().height))
