import pygame
import os


class Base:
    """
    This class represents the Base
    """
    IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")).convert_alpha())

    def __init__(self):
        """
        Initialize the base object
        """
        self.img = self.IMG