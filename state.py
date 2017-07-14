class State:

    S_MENU = 0
    S_GAME = 1

    SCENES = {
        S_MENU: 'MENU',
        S_GAME: 'GAME',
    }

    def __init__(self):
        self.scene = SCENES[S_MENU]
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()