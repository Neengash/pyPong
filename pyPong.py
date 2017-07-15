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

    def general_game_init(self):
        # center the screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(CAPTION)

    def general_game_end(self):
        pygame.quit()

    def check_exit(self):
        if self.state.exit_conditions():
            self.state.stop_running()

    def run(self):
        while self.state.is_running():
            self.state.load_inputs()
            self.state.clock_tick(self.state.get_fps())
            self.state.reset_screen()
            nscene = self.state.scene_loop()
            pygame.display.flip()
            self.check_exit()
        self.general_game_end()


if __name__ == '__main__':
    PyPong().run()
