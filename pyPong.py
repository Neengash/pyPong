import pygame
from pygame.locals import *
from menu import Menu
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
            if (event.type == pygame.QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.state['running'] = False

    def run(self):
        while self.state['runnig']:
            self.clock.tick(self.fps)
            nscene = self.scene.loop(state)

            if nscene is not None and nscene != self.scene.get_name() :
                self.load_new_scene()

            self.check_exit()

        self.general_game_end()


if __name__ == '__main__':
    PyPong().run()
