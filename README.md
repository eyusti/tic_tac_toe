# Tic Tac Toe AIs

This is the first of a series of projects that I am using to learn how to build optimized game AIs. For each project I'll be building out a number of AIs for each game and pitting them against each other to see how well they perform. 

Tic Tac Toe is a great starting ground  since the game is solved (a player can always draw) and also because the game state space (3^9 or 196839) is small and easily searchable.

Because it is solved, pitting AIs against each other at the most optimized end of the spectrum is rather boring since it is pretty easy to either script move rules or use min-max to never loose a game. That being said, this implementation also includes a few other AI "levels" of difficulty.

**Beginner**: Moves selected by RNG
**Intermediate**: If there is a spot where the opponent can actively win, it will block that spot, otherwise it will default to RNG
**Advanced**: Will prioritize a move that wins then game then one that blocks an opponent win. If neither exists, it will default to RNG
**Expert**: Min-Max algorithm implementation with alpha-beta pruning (aka this one should always at least draw)

## Win Optimization Results
Based on 1,000 games played between the AIs, here are some interesting take aways:

There are a total of 138 terminal board states in Tic Tac Toe. If you are the player to make the first move, 91 of those terminal states are winners, 44 are losers and three are ties. On paper, this means that there should be a pretty significant first player bias and the data backs this up:

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
B                1          596  0.596
B                2          283  0.283
Tie                         121  0.121

```

Given two AIs playing at random, the first player has a distinct advantage. This advantage is maintained when playing the same non-random AIs against themselves. However, the more heuristics applied to the AIs play (and therefore "better" the AI) the more tie situations were forced.

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
I                1          777  0.777
I                2           47  0.047
Tie                         176  0.176

AI      Turn order    Games won      %
----  ------------  -----------  -----
A                1          292  0.292
A                2          125  0.125
Tie                         583  0.583

AI      Turn order    Games won    %
----  ------------  -----------  ---
E                1            0    0
E                2            0    0
Tie                        1000    1
```

This appears to hold as you look at different permutations of AIs playing against each other.

*Random algorithm as player 1*
```
AI      Turn order    Games won     %       AI      Turn order    Games won      %
----  ------------  -----------  ----       ----  ------------  -----------  -----
B                1          770  0.77       B                1          308  0.308
I                2           60  0.06       A                2          130  0.13
Tie                         170  0.17       Tie                         562  0.562

*Non-random algorithm as player 1*
AI      Turn order    Games won       %     AI      Turn order    Games won       %
----  ------------  -----------  ------     ----  ------------  -----------  ------
I                1         5876  0.5876     A                1         5940  0.594
B                2         2887  0.2887     B                2         2811  0.2811
Tie                        1237  0.1237     Tie                        1249  0.1249
```

Given the same turn order, an incremental improvement in the AI results in greater wins for that AI. Across the board there are more ties. 

>Note: there was a lot of variance in runs when the non-random algorithm is player 1 at 100 games. The greater win rate between the intermediate and advanced AI would flip almost every batch. It seems to be a bit more stable in runs of 10,000 which is what is reported on above.

## Other Notes and Takeaways
python 3.6 

This implementation includes a human player mode for bonus fun. I used this mode to do ad hoc testing so test coverage of this project was pretty low. While fun, future AI projects will likely not have a human player mode to simplify codebase and have more robust test coverage.

There is also a re-write of min-max in a more negamax format implementation that takes advantage of the zero sum property of Tic Tac Toe.



