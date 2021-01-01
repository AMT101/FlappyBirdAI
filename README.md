# FlappyBirdAI
And AI bot that learns and plays flappy bird using NeuroEvolution.

# Instructions
Just run the game.py file and then the AI will start training automatically.

# Working Overview
The eval_genomes funciton is called a given number of times with a specified number of genomes and preinitialized configuration settings. The neural network and genome for each bird is kept in external lists which are modified according to the performance of each bird.
After one call to the eval_genomes function is over, the resulting population is determined from the best performes of the previous population with some mutation. The following screen shots show the initial and intermediate stage of the whole process.

![Alt text](https://gdurl.com/94YB "Initial State")
![Alt text](https://gdurl.com/Ts9X "Intermediate State")
