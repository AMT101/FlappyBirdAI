# FlappyBirdAI
And AI bot that learns and plays flappy bird using NeuroEvolution.

# Instructions
Just run the game.py file and then the AI will start training automatically.

# Features
- Pixel perfect collision
- Object pooling for optimization

# Working Overview
The eval_genomes funciton is called a given number of times with a specified number of genomes and preinitialized configuration settings. Then the neural network and genome for each bird is kept in external lists which are modified according to the performance of each bird.
After one call to the eval_genomes function is over, the resulting population is created from the best performers of the previous population with some mutation. The following screen shots show the initial and intermediate stage of the whole process.

This is the Initial state of the birds(before any training)
![Alt text](https://gdurl.com/HeYR "Initial State")

This is the intermediate state of the birds after training for 2 generations
![Alt text](https://gdurl.com/Ts9X "Intermediate State")
