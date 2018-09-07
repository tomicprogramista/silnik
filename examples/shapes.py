import setup_path  # example-specific, you won't need this in your code

import pygame
# import random
from random import randint

from silnik.image import Image
from silnik.rendering.point import Point
from silnik.rendering.shape import Polygon, rectangle

width, height = (800, 600)

pygame.init()
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

def random_color():
    return [
        randint(0, 255)
        for _ in range(3)
    ]

def random_point():
    return Point(
        randint(0, width),
        randint(0, height)
    )

def random_polygon():
    minimum = 2  # a 2-point polygon is a line
    maximum = 8  # let's not go too crazy, octagons are weird enough
    return Polygon([
        random_point()
        for _ in range(minimum, maximum)
    ])

shapes = [
    random_polygon()
    for _ in range(4)
]

images = [
    Image.create(shape, random_color())
    for shape in shapes
]

print("Press Ctrl-C to exit.")

while True:
    for image in images:
        screen.blit(image.raw_image, (image.shape.x, image.shape.y))
    pygame.display.update()
    clock.tick(60)
