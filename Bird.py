import pygame
import os


class Bird:
    """
    This class represents the flappy bird
    """
    IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", f"bird{x}.png"))) for x in range(1, 4)]

    def __init__(self):
        """
        Initialize the bird object
        """
        self.img = self.IMGS[0]
