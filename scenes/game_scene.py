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
        ball_scored = 0
        for actor in self.actors:
            actor.update()

            if isinstance(actor, Ball):
                if actor.check_out_left():
                    self.p2_score()
                    self.actors.remove(actor)
                    ball_scored = 2
                elif actor.check_out_right():
                    self.p1_score()
                    self.actors.remove(actor)
                    ball_scored = 1
        if ball_scored and not self.win:
            # IF player 2 scored new ball is for player 1
            # And viceversa.
            self.new_ball(1 if ball_scored == 2 else 2)

    def p1_score(self):
        self.score[0] += 1
        if self.score[0] == 9:
            self.raise_win(1)

    def p2_score(self):
        self.score[1] += 1
        if self.score[1] == 9:
            self.raise_win(2)

    def raise_win(self, player):
        print("player {} wins".format(player))

    def new_ball(self, player):
        ball = Ball(self.state)
        ball.set_ball_for_player(player)
        self.actors.append(ball)

    def draw(self):
        self.draw_scenario()
        for actor in self.actors:
            actor.draw()

    def draw_scenario(self):
        screen = self.state.get_screen()
        pygame.draw.line(screen, (255, 255, 255),
            (screen.get_rect().width / 2, 0),
            (screen.get_rect().width / 2, screen.get_rect().height))
