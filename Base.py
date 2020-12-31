import pygame
import os


class Base:
    """
    This class represents the Base
    """
    IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")).convert_alpha())
    VEL = 5
    WIDTH = IMG.get_width()

    def __init__(self, y):
        """
        Initialize the base object
        :param y: y-coordinate of the base
        :return: None
        """
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        """
        Moving the two floor images to make it look like a neverending surface
        :return: None
        """
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        """
        Drawing the floor
        :param win: pygame window
        :return: None
        """
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
