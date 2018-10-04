import pygame

from .colors import Colors
from .point import Point
from .shape import rectangle

class Text:
    def __init__(self, content, font_size=12, font_color=None):
        self.content = content
        self.font_size = font_size
        self.font_color = font_color or Colors.BLACK

    def font(self):
        return pygame.font.SysFont('Arial', self.font_size)

    def pre_render(self):
        return self.font().render(self.content, False, self.font_color)