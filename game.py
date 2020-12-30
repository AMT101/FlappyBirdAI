import pygame
import os

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
DRAW_LINES = False

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "bg.png")).convert_alpha(), (600, 900))


def draw_window(win, bird):
    win.blit(bg_img, (0, 0))
    bird.draw(win)
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

    bird = Bird(250, 300)
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
        draw_window(WIN, bird)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
