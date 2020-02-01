# Tic Tac Toe AIs

This is the first of a series of projects that I am using to learn how to build optimized game AIs. For each project I'll be building out a number of AIs for each game and pitting them against each other to see how well they perform. 

Tic Tac Toe is a great starting ground  since the game is solved (a player can always draw) and also because the game state space (3^9 or 196839) is small and easily searchable.

Because it is solved, pitting AIs against each other at the most optimized end of the spectrum is rather boring since it is pretty easy to either script move rules or use min-max to never loose a game. That being said, this implementation also includes a few other AI "levels" of difficulty.

>**Beginner (B)**: Moves selected by RNG

>**Intermediate Defensive (ID)**: If there is a spot where the opponent can actively win, it will block that spot, otherwise it will default to RNG  

>**Intermediate Offensive (IO)**: If there is a spot where the AI can actively win, it will take that spot, otherwise it will default to RNG

>**Advanced (A)**: Will prioritize a move that wins then game then one that blocks an opponent win. If neither exists, it will default to RNG  

>**Expert (E)**: Min-Max algorithm implementation with alpha-beta pruning (aka this one should always at least draw)


## Win Optimization Results
Based on 1,000 games played between the AIs, here are some interesting take aways:

There are a total of 138 terminal board states in Tic Tac Toe. If you are the player to make the first move, 91 of those terminal states are winners, 44 are losers and three are ties. On paper, this means that there should be a pretty significant first player bias and the data backs this up:

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
B                1          595  0.595
B                2          287  0.287
Tie                         118  0.118

```

Given two AIs playing at random, the first player has a distinct advantage. This advantage is maintained when playing the same non-random AIs against themselves. With the notable exception of the intermediate offensive AI.

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
ID               1          783  0.783
ID               2           56  0.056
Tie                         161  0.161

AI      Turn order    Games won      %
----  ------------  -----------  -----
IO               1          222  0.222
IO               2          361  0.361
Tie                         417  0.417

AI      Turn order    Games won      %
----  ------------  -----------  -----
A                1          314  0.314
A                2          124  0.124
Tie                         562  0.562

AI      Turn order    Games won    %
----  ------------  -----------  ---
E                1            0    0
E                2            0    0
Tie                        1000    1
```

It's also interesting to take a look at the itermediate defensive, intermediate offensive, and advanced AIs against the benchmarks of the RNG beginner AI and the expert AI that should always at least tie. 

*Random/expert algorithm as player 1*
```
AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
B                1          401   B                1          109   B                1          120
ID               2          511   IO               2          437   A                2          467
Tie                          88   Tie                         454   Tie                         413

AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
E                1          999   E                1          863   E                1          855
ID               2            0   IO               2            0   A                2            0
Tie                           1   Tie                         137   Tie                         145
```

*Non-random algorithm as player 1*
```
AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
ID               1          802   IO               1          790   A                1          899
B                2           24   B                2          174   B                2           10
Tie                         174   Tie                          63   Tie                          91

AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
ID               1            0   IO               1            0   A                1            0
E                2          192   E                2          800   E                2          198
Tie                         808   Tie                         200   Tie                         802
```

There are a couple of interesting behaviors here. The first is that the beginner algorithm seems to outright win more against the advanced AI in comparison to the intermediate offensive AI. 

The second is that when the expert AI goes first, the offensive intermediate AI and advanced AI perform similary (while the intermediate defense AIs performance tanks) but when the expert AI goes second the advanced and defensive intermediate AIs perform very similarly (with the intermediate offensive AI tanking). 

## Other Notes and Takeaways
python 3.6 

This implementation includes a human player mode for bonus fun. I used this mode to do ad hoc testing so test coverage of this project was pretty low. While fun, future AI projects will likely not have a human player mode to simplify codebase and have more robust test coverage.

There is also a re-write of min-max in a more negamax format implementation that takes advantage of the zero sum property of Tic Tac Toe.



