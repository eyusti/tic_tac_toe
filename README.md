# Tic Tac Toe AIs

This is the first in a series of projects where I'm building AIs for games. For each project, I'll build out a number of AIs for each game and pit them against each other to see how well they perform. 

Tic Tac Toe is a great game to start with since it is solved (either player can force a draw) and because the game state space is small ( < 3^9 = 196839), and fully searchable.

## Tic Tac Toe AI Variations

**Beginner (B)**: Random move selection

**Intermediate Defensive (ID)**: If there is a spot where the opponent can actively win, it will block that spot, otherwise it will default to RNG  

**Intermediate Offensive (IO)**: If there is a spot where the AI can actively win, it will take that spot, otherwise it will default to RNG

**Advanced (A)**: Will prioritize a move that wins the game, then one that blocks an opponent win. If neither exists, it will default to RNG  

**Expert (E)**: Min-Max algorithm implementation with alpha-beta pruning (always at least draws)

## AI Battleground Takeaways

Tic Tac Toe is a pretty thoroughly explored game so I can't say there were any revolutionary takeaways. However, there were a few interesting notes I wanted to highlight.

### A couple good heuristics go a long way

Adding the instructions to block a win and to actively win went a long way. It is tempting to keep scripting additional instructions (you can fully script a game of Tic Tac Toe to always win), but even the most basic instructions improve performance significantly.

```
AI      Turn order    Games won     AI      Turn order    Games won
----  ------------  -----------     ----  ------------  -----------
B                1            0     A                1            0
E                2          819     E                2          196
Tie                         181     Tie                         804

AI      Turn order    Games won     AI      Turn order    Games won
----  ------------  -----------     ----  ------------  -----------
E                1          997     E                1          880  
B                2            0     A                2            0
Tie                           3     Tie                         120
```

### Interesting Outlier

As I was playing the AIs against each other, I noticed one interesting outlier. 

```
AI      Turn order    Games won   AI      Turn order    Games won   AI      Turn order    Games won 
----  ------------  -----------   ----  ------------  -----------   ----  ------------  ----------- 
B                1          595   IO               1          657   ID               1          215 
B                2          287   IO               2          291   ID               2           82 
Tie                         118   Tie                          52   Tie                         703 

AI      Turn order    Games won   AI      Turn order    Games won
----  ------------  -----------   ----  ------------  -----------
A                1          324   E                1            0
A                2          167   E                2            0
Tie                         509   Tie                        1000
```

In all cases of an AI playing against itself, more of the results ended in ties than the purely random game except in the case of the offensive intermediate AI. Instead, in this case, more games are converting to wins for both players in proportion to the first player advantage you see in all the above games. 

This makes a lot of sense since this AI is largely going to be playing randomly since it won't encounter multiple winnable positions allowing it to make more than one informed choice. However, since it is able to actualize a win when it sees one, it is more likely that games would end in a win for either player than to randomly end up at a board with a tie (based on the result distribution of terminal board states). Additionally, the first player is eventually more likely to be presented with a winning board so they have the  advantage. 

> There are a total of 138 terminal board states in Tic Tac Toe. If you are the player to make the first move, 91 of those terminal states are winners, 44 are losers and 3 are ties. <sup>[FROM WIKIPEDIA](https://en.wikipedia.org/wiki/Tic-tac-toe#Combinatorics)</sup>

## Other Notes and Takeaways
python 3.6 

This implementation includes a human player mode for bonus fun if you want to test your Tic Tac Toe skills. I used this mode to do ad hoc testing so test coverage of this project is basically non-existant. 

There is also a commented out rewrite of min-max that follow the negamax format if you want to check out what that would look like.


