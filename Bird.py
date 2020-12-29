import pygame
import os
import math


class Bird:
    """
    This class represents the flappy bird
    """
    IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", f"bird{x}.png"))) for x in range(1, 5)]
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        """
        Initializes the Bird object
        :param x: x-coordinate of the bird's current position
        :param y: y-coordinate of the bird's current position
        :return: None
        """
        self.x = x
        self.y = y
        self.img = self.IMGS[0]
        self.vel = 0
        self.tilt = 0
        self.ticks = 0
        self.height = self.y
        self.img_count = 0

    def draw(self, win):
        """
        Displays bird object on the window
        :param win: pygame window
        :return: None
        """

        # For animating the bird flapping
        if self.ANIMATION_TIME*4 <= self.img_count:
            self.img = self.IMGS[0]
            self.img_count = 0
        else:
            ind = math.floor(self.img_count / self.ANIMATION_TIME)
            self.img = self.IMGS[ind]

        # For the time when the bird is free falling
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2 - 1

        self.img_count += 1

        # rotating the image
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        """
        get the mask for the current image of the bird
        :return: mask of the bird
        """
        return pygame.mask.from_surface(self.img)



