# Tic Tac Toe AIs

This is the first of a series of projects that I am using to learn how to build optimized game AIs. For each project I'll be building out a number of AIs for each game and pitting them against each other to see how well they perform. 

Tic Tac Toe is a great starting ground  since the game is solved (a player can always draw) and also because the game state space (3^9 or 196839) is small and easily searchable.

Because it is solved, pitting AIs against each other at the most optimized end of the spectrum is rather boring since it is pretty easy to either script move rules or use min-max to never loose a game. That being said, this implementation also includes a few other AI "levels" of difficulty.

**Beginner**: Moves selected by RNG
**Intermediate**: If there is a spot where the opponent can actively win, it will block that spot, otherwise it will default to RNG
**Advanced**: Will prioritize a move that wins then game then one that blocks an opponent win. If neither exists, it will default to RNG
**Expert**: Min-Max algorithm implementation with alpha-beta pruning (aka this one should always at least draw)

## Win Optimization Results

## Time Optimization Results

## Other Notes and Takeaways
python 3.6 

This implementation includes a human player mode for bonus fun. I used this mode to do ad hoc testing so test coverage of this project was pretty low. While fun, future AI projects will likely not have a human player mode to simplify codebase and have more robust test coverage.

