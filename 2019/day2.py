import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from intcode import runIntcode


def main():
    
    code = parseInput("input.txt")

    code[1] = 12
    code[2] = 2
    part1 = runIntcode(code)
    print(part1[0])

    found = False
    for i in range(100):
        for j in range(100):
            code[1] = i
            code[2] = j
            x = runIntcode(code)
            if x[0] == 19690720:
                print(100 * i + j)
                found = True
                break
        if found:
            break


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]
    

if __name__ == "__main__":
    main()