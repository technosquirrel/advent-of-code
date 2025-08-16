import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import intcode
from itertools import permutations


def main():
    
    code = parseInput("input.txt")
    opts = list(permutations(range(5)))
    
    part1 = 0
    for sequence in opts:
        output = [0]
        for signal in sequence:
            output = intcode.runIntcode(code, [signal, output[-1]])
        if output[-1] > part1:
            part1 = output[-1]

    print(part1)

    opts2 = list(permutations(range(5, 10)))
    part2 = 0

    for sequence in opts2:
        inputs = [[x] for x in sequence]
        inputs[0].append(0)
        n = intcode.runLoop(code, inputs)
        if n > part2:
            part2 = n

    print(part2)



def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]


if __name__ == "__main__":
    main()