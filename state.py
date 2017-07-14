import pygame
from scenes.game_scene import Game_scene as game
from scenes.menu import Menu

class State:

    S_MENU = 0
    S_GAME = 1

    def __init__(self):
        self.init_scene(State.S_MENU)
        self.running = True
        self.clock   = pygame.time.Clock()
        self.screen  = pygame.display.get_surface()
        self.keys    = None

    def init_scene(self, scene_code):
        if scene_code == State.S_MENU:
            self.scene = Menu()
        elif scene_code == State.S_GAME:
            self.scene = Game()

    def start_running(self):
        self.running = True

    def stop_running(self):
        self.running = False

    def is_running(self):
        return self.running

    def scene_loop(self, state):
        self.scene.loop_step(state)

    def clock_tick(self, fps):
        self.clock.tick(fps)

    def get_screen(self):
        return self.screen

    def reset_screen(self):
        self.screen.fill(pygame.Color("black"))

    def load_keys(self):
        self.events = pygame.event.get()
        self.keys = pygame.key.get_pressed()

    def exit_conditions(self):
        for event in self.events:
            if ((event.type == pygame.QUIT) or
                (self.keys[pygame.K_ESCAPE])):
                return True
        return False
