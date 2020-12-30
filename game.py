import pygame
import os

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
DRAW_LINES = False

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "bg.png")).convert_alpha(), (600, 900))

PIPE_QUEUE = []


class ObjectPooler:
    PIPE_QUEUE = []

    def add_pipe(self, pipe):
        """
        Adds the pipe that has gone out of the window to PIPE_QUEUE to be used again
        :param pipe: pipe object that has gone out of the window
        :return: None
        """
        self.PIPE_QUEUE.append(pipe)


def draw_window(win, bird, pipe):
    win.blit(bg_img, (0, 0))
    bird.draw(win)
    pipe.draw(win)

    pygame.display.update()


def main():
    """
    main thread to run first
    :return: None
    """
    # objects to be used once the display loads
    from Bird import Bird
    from Pipe import Pipe
    from Base import Base

    obj_pooler = ObjectPooler()
    bird = Bird(250, 300)
    pipe = Pipe(WIN_WIDTH+30, WIN_HEIGHT, WIN_WIDTH, obj_pooler)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.jump()

        bird.move()
        if obj_pooler.PIPE_QUEUE:
            new_pipe = obj_pooler.PIPE_QUEUE.pop()
            new_pipe.set_reset_pipe(WIN_WIDTH+30)
        pipe.move()
        if pipe.collide(bird):
            print("Bird ded!!")

        draw_window(WIN, bird, pipe)
    pygame.quit()
    quit()


if __name__ == '__main__':
    PIPE_QUEUE= []
    main()
