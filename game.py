import pygame
import os
import neat

pygame.font.init()  # initializing font

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
PIPE_GAP = 400
DRAW_LINES = False

STAT_FONT = pygame.font.SysFont("comicsans", 50)

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "bg.png")).convert_alpha(), (600, 900))

gen = 0

class ObjectPooler:
    PIPE_QUEUE = []

    def add_pipe(self, pipe):
        """
        Adds the pipe that has gone out of the window to PIPE_QUEUE to be used again
        :param pipe: pipe object that has gone out of the window
        :return: None
        """
        self.PIPE_QUEUE.append(pipe)


def draw_window(win, birds, pipes, base, score, gen, pipe_ind):
    win.blit(bg_img, (0, 0))

    for bird in birds:
        bird.draw(win)

    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)

    # score
    score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    pygame.display.update()


def eval_genomes(genomes, config):
    """
    runs the simulation of the current population of birds
    :return: None
    """
    # objects to be used once the display loads
    from Bird import Bird
    from Pipe import Pipe
    from Base import Base

    global WIN, gen
    gen += 1

    # start by creating lists holding the genome itself, the
    # neural network associated with the genome and the
    # bird object that uses that network to play
    nets = []
    birds = []
    ge = []

    for genome_id, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(250, 300))
        ge.append(genome)

    obj_pooler = ObjectPooler()
    # bird = Bird(250, 300)
    pipes = [Pipe(WIN_WIDTH+30, WIN_HEIGHT, WIN_WIDTH, obj_pooler)]
    base = Base(WIN_HEIGHT-150)
    score = 0

    clock = pygame.time.Clock()

    run = True
    while run and len(birds) > 0:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # elif event.type == pygame.KEYDOWN:  # For manual control
            #     if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            #         bird.jump()

        # determining the pipe to be used for NN input
        pipe_ind = 0
        min_dist = WIN_WIDTH + 50
        for i, pipe in enumerate(pipes):
            if birds:
                if min_dist > pipe.x + pipe.TOP_PIPE.get_width() > birds[0].x:
                    min_dist = pipe.x
                    pipe_ind = i

        for x, bird in enumerate(birds):    # increases the fitness score of each bird that has survived the frame
            ge[x].fitness += 0.1
            bird.move()

            # send bird location, top pipe location and bottom pipe location
            # and determine from network whether to jump or not
            output = nets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:
                bird.jump()

        base.move()

        # to increment the score variable
        add_pipe = False
        for pipe in pipes:
            for bird in birds:
                if not pipe.passed and bird.x > pipe.x + pipe.TOP_PIPE.get_width():
                    pipe.passed = True
                    add_pipe = True

                if pipe.collide(bird):
                    # not letting the collided birds have impact on the weights
                    x = birds.index(bird)
                    ge[x].fitness -= 1
                    nets.pop(x)
                    ge.pop(x)
                    birds.pop(x)

        if add_pipe:
            score += 1
            # rewarding birds more for passing through a pipe
            for genome in ge:
                genome.fitness += 5

        # creating multiple pipes with gap specified by PIPE_GAP
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

        # removing birds that touched the floor or try to fly out of the screen to go above the pipes
        for bird in birds:
            if bird.y + bird.img.get_height() - 10 >= base.y or bird.y < -50:
                nets.pop(birds.index(bird))
                ge.pop(birds.index(bird))
                birds.pop(birds.index(bird))
        draw_window(WIN, birds, pipes, base, score, gen, pipe_ind)

    if not run:
        pygame.quit()
        quit()


def run(config_file):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(eval_genomes, 50)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)