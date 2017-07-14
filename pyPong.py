import os
import pygame
from pygame.locals import *
from scenes.menu import Menu
from state import State

CAPTION = 'PY-PONG'

class PyPong:

    width = 640
    height = 480

    def __init__(self):
        self.general_game_init()
        self.state = State()
        self.fps = 60

    def general_game_init(self):
        # center the screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(CAPTION)

    def general_game_end(self):
        pygame.quit()

    def check_exit(self):
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT) or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.state.stop_running()

    def run(self):
        while self.state.is_running():
            self.state.clock_tick(self.fps)
            nscene = self.state.scene_loop(self.state)
            pygame.display.flip()
            self.check_exit()
        self.general_game_end()


if __name__ == '__main__':
    PyPong().run()
