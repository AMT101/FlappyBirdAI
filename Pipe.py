import pygame
import os
import random
import game


class Pipe:
    """
    This class represents the Pipe
    """
    IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")).convert_alpha())
    GAP = 250
    VEL = 5

    def __init__(self, x, win_height, win_width):
        """
        Initializes the Pipe object
        :param x: initial x-coordinate of the pipe's position
        :param win_height: Height of the window created
        """
        self.img = self.IMG
        self.x = x
        self.win_height = win_height
        self.win_width = win_width

        self.top = 0
        self.bottom = 0

        self.TOP_PIPE = pygame.transform.flip(self.IMG, False, True)
        self.BOTTOM_PIPE = self.IMG

        self.passed = False
        self.out_screen = False

        self.set_height()

    def set_height(self):
        """
        Sets the height of the pipe from the top of the screen
        :return: None
        """
        self.height = random.randrange(50, self.win_height-50)
        self.top = self.height - self.TOP_PIPE.get_height()
        self.bottom = self.height + self.GAP


    def move(self):
        """
        Moves the pipe leftwards with constant velocity
        :return: None
        """
        self.x -= self.VEL
        # if pipe passes the screen
        if self.x < -20 and not self.out_screen:
            self.out_screen = True
            self.reset()

    def reset(self):
        """
        resets the initial state of the pipe to be used again (Object Pooling)
        :return: None
        """
        self.passed = False
        game.add_pipe(self)

    def set_reset_pipe(self, x):
        """
        Function to be used by the main module, to reset the state of the pipe
        :param x: x-coordinate of the pipe
        :return: None
        """
        self.x = x
        self.out_screen = False
        self.set_height()


    def draw(self, win):
        """
        Draw the pipes
        :param win: pygame window
        :return: None
        """
        # draw top
        win.blit(self.TOP_PIPE, (self.x, self.top))
        # draw bottom
        win.blit(self.BOTTOM_PIPE, (self.x, self.bottom))






