import pygame
from pygame.locals import *
import menu
import game

CAPTION = 'PY-PONG'

class PyPong:

    width = 640
    height = 480

    S_MENU = 0
    S_GAME = 1

    SCENES = {
        S_MENU: 'MENU',
        S_GAME: 'GAME',
    }

    def __init__(self):
        self.general_game_init()
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.done = False
        self.fps = 60
        self.scene = Menu()

    def general_game_init(self):
        # center the screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_mode([self.witdh, self.height])
        pygame.display.set_caption(CAPTION)

    def general_game_end(self):
        pygame.quit()

    def check_exit(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.done = True

    def run(self):
        while not self.done:
            self.clock.tick(self.fps)
            nscene = self.scene.loop()

            if nscene != self.scene.get_name() :
                self.load_new_scene()

            self.check_exit()

        self.general_game_end()


if __name__ == '__main__':
    PyPong().run()