import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import intcode

DIRS = {
    "U" : (-1, 0),
    "D" : (1, 0),
    "L" : (0, -1),
    "R" : (0, 1)
}

ORDER = ["U", "R", "D", "L"]

def main():
    
    code = parseInput("input.txt")

    copy = {i : x for i, x in enumerate(code)}
    index = 0
    base = 0
    inputs = []

    position = (0, 0)
    direction = "U"
    floor = {}
    state = "paint"

    while True:
        outs = intcode.runInstruction(copy, index, inputs, base)
        if not "pos" in outs:
            if position in floor:
                inputs.append(floor[position])
            else:
                inputs.append(0)
        else:
            index = outs["pos"]
        if "out" in outs:
            if state == "paint":
                floor[position] = outs["out"]
                state = "turn"
            elif state == "turn":
                direction = turn(outs["out"], direction)
                position = move(position, direction)
                state = "paint"
            else:
                raise ValueError
        if "halt" in outs:
            break
        if "base" in outs:
            base = outs["base"]

    print(len(floor))

    copy = {i : x for i, x in enumerate(code)}
    index = 0
    base = 0
    inputs = [1]

    position = (0, 0)
    direction = "U"
    floor = {}
    state = "paint"

    while True:
        outs = intcode.runInstruction(copy, index, inputs, base)
        if not "pos" in outs:
            if position in floor:
                inputs.append(floor[position])
            else:
                inputs.append(0)
        else:
            index = outs["pos"]
        if "out" in outs:
            if state == "paint":
                floor[position] = outs["out"]
                state = "turn"
            elif state == "turn":
                direction = turn(outs["out"], direction)
                position = move(position, direction)
                state = "paint"
            else:
                raise ValueError
        if "halt" in outs:
            break
        if "base" in outs:
            base = outs["base"]

    h = max(floor, key=lambda x : x[0])[0]
    w = max(floor, key=lambda x : x[1])[1]

    message = [[" " for _ in range(w + 1)] for _ in range(h + 1)]
    for tile in floor:
        if floor[tile] == 1:
            message[tile[0]][tile[1]] = "#"

    for line in message:
        print("".join(line))


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]
    

def turn(n, dir):

    i = ORDER.index(dir)

    if n == 0:
        i = (i - 1) % 4
    elif n == 1:
        i = (i + 1) % 4
    else:
        raise ValueError
    
    return ORDER[i]


def move(pos, dir):
    return (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])


if __name__ == "__main__":
    main()