import pygame
from custom_enums import Color


class Window:

    def __init__(self, width, height, border=1):
        pygame.init()
        self.screen = pygame.display.set_mode([width, height])
        self.border_size = border
        self.screen.fill(Color.WHITE.value)

    def run(self):

        pygame.display.flip()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def draw_rect(self, inner_color: Color, x, y, width, height):
        pygame.draw.rect(self.screen,
                         Color.BLACK.value,
                         pygame.Rect(x, y, width, height))
        pygame.draw.rect(self.screen,
                         inner_color.value,
                         pygame.Rect(x + self.border_size,
                                     y + self.border_size,
                                     width - (self.border_size * 2),
                                     height - (self.border_size * 2)))