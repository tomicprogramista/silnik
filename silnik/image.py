import random

import numpy as np
import pygame

from .rendering.point import Point
from .rendering import shape

class Image:
    """
    A wrapper around a pygame image class. It provides a common interface for
    drawable elements.

    The code outside of this class should not use any other image-related APIs.
    """
    DEFAULT_COLOR = (0, 0, 0)

    def __init__(self, raw_image, shape):
        self.raw_image = raw_image
        self.shape = shape

    @classmethod
    def load(cls, path):
        """
        Loads and prepares an image from a local file
        """
        raw_image = pygame.image.load(path)
        raw_image.convert_alpha()

        pyrect = raw_image.get_rect()

        rectangle = shape.rectangle(
            Point(pyrect.left, pyrect.top),
            Point(pyrect.right, pyrect.bottom)
        )
        
        return Image(
            raw_image,
            rectangle)

    @classmethod
    def create(cls, shape, color=None):
        """
        Creates a new surface from `shape`
        """
        mask = shape.build_surface_mask()

        width = mask.shape[0]
        height = mask.shape[1]

        # pygame coordinates are a transpose of numpy's system
        mask = mask.transpose()

        # Set pixels outside of the figure as fully transparent (requires a per-pixel alpha value)
        surface = pygame.Surface(
            (width, height),
            flags=pygame.SRCALPHA)

        # `surface.fill` has to be called *before* setting alpha values
        color = color or cls.DEFAULT_COLOR
        surface.fill(color)

        alpha = pygame.surfarray.pixels_alpha(surface)
        alpha[:] = mask * 255

        return Image(surface, shape)
