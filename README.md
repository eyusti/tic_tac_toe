# Tic Tac Toe AIs

This is the first of a series of projects that I am using to learn how to build optimized game AIs. For each project I'll be building out a number of AIs for each game and pitting them against each other to see how well they perform. 

Tic Tac Toe is a great starting ground  since the game is solved (a player can always draw) and also because the game state space (3^9 or 196839) is small and easily searchable.

Because it is solved, pitting AIs against each other at the most optimized end of the spectrum is rather boring since it is pretty easy to either script move rules or use min-max to never lose a game. That being said, this implementation also includes a few other AI "levels" of difficulty.

**Beginner (B)**: Moves selected by RNG

**Intermediate Defensive (ID)**: If there is a spot where the opponent can actively win, it will block that spot, otherwise it will default to RNG  

**Intermediate Offensive (IO)**: If there is a spot where the AI can actively win, it will take that spot, otherwise it will default to RNG

**Advanced (A)**: Will prioritize a move that wins the game then one that blocks an opponent win. If neither exists, it will default to RNG  

**Expert (E)**: Min-Max algorithm implementation with alpha-beta pruning (aka this one should always at least draw)

## Win Optimization Results
Based on 1,000 games played between the AIs, here are some interesting takeaways:

There are a total of 138 terminal board states in Tic Tac Toe. If you are the player to make the first move, 91 of those terminal states are winners, 44 are losers and three are ties. On paper, this means that there should be a pretty significant first player bias and the data backs this up:

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
B                1          595  0.595
B                2          287  0.287
Tie                         118  0.118

```

Given two AIs playing at random, the first player has a distinct advantage. This advantage is maintained when playing the same non-random AIs against themselves. 

```
AI      Turn order    Games won      %
----  ------------  -----------  -----
IO               1          657  0.657
IO               2          291  0.291
Tie                          52  0.052

AI      Turn order    Games won      %
----  ------------  -----------  -----
ID               1          215  0.215
ID               2           82  0.082
Tie                         703  0.703

AI      Turn order    Games won      %
----  ------------  -----------  -----
A                1          324  0.324
A                2          167  0.167
Tie                         509  0.509

AI      Turn order    Games won    %
----  ------------  -----------  ---
E                1            0    0
E                2            0    0
Tie                        1000    1
```

It seems that the "better" the AI is, the more draws you see as it plays against itself. The exception to this hypothesis is the intermediate offensive AI as it draws less against itself than the random beginner AI playing against itself. You would expect the offensive AI to be "better" than random since there is more information being used in decision making. 

To dive deeper into whether the intermediate offensive AI provides a heuristic improvement over random play, let's take a look at the intermediate defensive, intermediate offensive, and advanced AIs against the benchmarks of beginner AI and the expert AI. 

*Random/expert algorithm as player 1*
```
AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
B                1          421   B                1          145   B                1           58
IO               2          502   ID               2          423   A                2          721
Tie                          77   Tie                         432   Tie                         221

AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
E                1          995   E                1          878   E                1          873
IO               2            0   ID               2            0   A                2            0
Tie                           5   Tie                         122   Tie                         127

```
This set of data provides some more nuance to the initial hypothesis. All of the AIs perform better than the beginner AI even though it has first player advantage. This leads us to believe that all of the AIs are at least a heuristic improvement over random. 

It also seems that the greater the number of ties when played against itself is a pretty good indicator of overall performance here. The offensive AI loses significantly more against the expert AI than the other AIs. The beginner AI also wins significantly more games against the offensive AI in comparison to the other AIs. Let's see if this holds when the AIs go first against the benchmarks.

*Non-random algorithm as player 1*
```
AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
IO               1          830   ID               1          804   A                1          884
B                2          113   B                2           23   B                2           13
Tie                          57   Tie                         173   Tie                         103

AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------   ----  ------------  -----------
IO               1            0   ID               1            0   A                1            0
E                2          817   E                2          193   E                2          186
Tie                         183   Tie                         807   Tie                         814
```

The previous analysis appears to hold here as well. You can see in both data sets that while the offensive AI outright wins more against the beginner AI than the defensive AI, it also has more outright losses in both cases. Similarly, the offensive AI fairs poorly against the expert AI. While the defensive also does not win any games, more of the outcomes are bucketed in ties rather than straight losses.

So, how do they fare against each other?

```
AI      Turn order    Games won      %     AI      Turn order    Games won      %
----  ------------  -----------  -----     ----  ------------  -----------  ----- 
IO               1          219  0.219     ID               1          775  0.775
ID               2          362  0.362     IO               2           63  0.063
Tie                         419  0.419     Tie                         162  0.162
```

Looks like the offensive AI is better than nothing, but is the worst performing of the AI options here.

## Other Notes and Takeaways
python 3.6 

This implementation includes a human player mode for bonus fun. I used this mode to do ad hoc testing so test coverage of this project was pretty low. While fun, future AI projects will likely not have a human player mode to simplify codebase and have more robust test coverage.

There is also a rewrite of min-max in a more negamax format implementation that takes advantage of the zero sum property of Tic Tac Toe.



