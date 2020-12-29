import pygame
import os


class Pipe:
    """
    This class represents the Pipe
    """
    IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")).convert_alpha())

    def __init__(self):
        """
        Initialize the pipe object
        """
        self.img = self.IMG