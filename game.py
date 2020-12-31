import pygame
import os

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
PIPE_GAP = 400
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


def draw_window(win, bird, pipes, base):
    win.blit(bg_img, (0, 0))
    bird.draw(win)

    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)

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
    pipes = [Pipe(WIN_WIDTH+30, WIN_HEIGHT, WIN_WIDTH, obj_pooler)]
    base = Base(WIN_HEIGHT-150)
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
        base.move()

        max_x = 0
        for pipe in pipes:
            max_x = max(pipe.x, max_x)
            
        if max_x < WIN_WIDTH - PIPE_GAP:
            if obj_pooler.PIPE_QUEUE:
                new_pipe = obj_pooler.PIPE_QUEUE.pop()
                new_pipe = new_pipe.set_reset_pipe(WIN_WIDTH+30)
            else:
                pipes.append(Pipe(WIN_WIDTH + 30, WIN_HEIGHT, WIN_WIDTH, obj_pooler))
        for pipe in pipes:
            pipe.move()

            if pipe.collide(bird):
                print("Bird ded!!")

        draw_window(WIN, bird, pipes, base)
    pygame.quit()
    quit()


if __name__ == '__main__':
    PIPE_QUEUE= []
    main()
