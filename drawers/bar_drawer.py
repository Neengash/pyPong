import pygame

class BarDrawer():

    def draw(self, posx, posy, width, height):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (255, 255, 255), [
            posx - width / 2,
            posy - height / 2,
            width,
            height
        ])
