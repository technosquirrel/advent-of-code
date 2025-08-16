import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import intcode

def main():
    
    code = parseInput("input.txt")
    print(intcode.runIntcode(code, [1]))
    print(intcode.runIntcode(code, [2]))


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]


if __name__ == "__main__":
    main()