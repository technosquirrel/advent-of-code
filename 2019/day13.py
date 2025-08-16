import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import intcode


def main():

    code = intcode.parseInput("input.txt")
    output = intcode.runIntcode(code)

    bricks = {}
    ball = 0
    paddle = 0

    for i in range(0, len(output), 3):
        if output[i + 2] == 2:
            bricks[(output[i], output[i + 1])] = True
        elif output[i + 2] == 3:
            paddle = [output[i], output[i + 1]]
        elif output[i + 2] == 4:
            ball = [output[i], output[i + 1]]

    print(len(bricks))

    #part2
    score = 0
    halt = False

    inputs = []
    base = 0
    pos = 0
    output = []
    moves = 0

    code[0] = 2
    while not halt:
        outs = intcode.runIntcode(code, inputs, base, pos, output)
        if outs[0] is False:
            chunk = outs[5]
            for i in range(0, len(chunk), 3):
                if chunk[i] == -1 and chunk[i + 1] == 0:
                    score = chunk[i + 2]
                    if len(bricks) == 0:
                        halt = True
                        break
                elif chunk[i + 2] == 4:
                    ball[0] = chunk[i]
                    ball[1] = chunk[i + 1]
                elif chunk[i + 2] == 3:
                    paddle[0] = chunk[i]
                    paddle[1] = chunk[i + 1]
                elif chunk[i + 2] == 0:
                    if (chunk[i], chunk[i + 1]) in bricks:
                        del bricks[(chunk[i], chunk[i + 1])]

            joystick = 0
            if ball[0] < paddle[0]:
                joystick = -1
            elif ball[0] > paddle[0]:
                joystick = 1

            moves += 1

            code = outs[1]
            inputs.append(joystick)
            base = outs[3]
            pos = outs[4]
            output = []        

    print(score, moves)


if __name__ == "__main__":
    main()