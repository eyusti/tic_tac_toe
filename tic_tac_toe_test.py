import pytest
from tic_tac_toe import Board, Game

def inc(x):
    return x + 1

counts={}
names={}
for line in sys.stdin.readlines():
    sp = line.split()
    if counts[sp[0]] is not None:
        counts[sp[0]] = counts[sp[0]] + 1
    else:
        ... = 1
    names[sp[0]] = names[sp[0]].append(sp[1])


def test_answer():
    assert inc(3) == 5