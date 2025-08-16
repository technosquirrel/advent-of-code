import math

def main():
    
    memory = [34615120, 0, 0]
    program = [2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0]

    print(",".join([str(x) for x in execute(0, program, memory)]))

    # part 2

    opts = [0]
    i = 1
    found = False
    while not found:
        newOpts = []
        for a in opts:
            for n in range(a, a + 8):
                if found:
                    break
                outs = execute(0, program, [n, 0, 0])
                if outs == program:
                    print(n)
                    found = True
                elif outs == program[-i:]:
                    newOpts.append(n * 8)
        opts = newOpts
        i += 1


def execute(i, program, memory):

    outs = []

    while i < len(program):

        opcode = program[i]
        x = getComboOperand(program[i + 1], memory)

        match opcode:
            case 0:
                memory[0] = math.trunc(memory[0] / pow(2, x))
            case 1:
                memory[1] = memory[1] ^ program[i + 1]
            case 2:
                memory[1] = x % 8
            case 3:
                if memory[0] != 0:
                    i = program[i + 1]
                    continue
            case 4:
                memory[1] = memory[1] ^ memory[2]
            case 5:
                outs.append(x % 8)
            case 6:
                memory[1] = math.trunc(memory[0] / pow(2, x))
            case 7:
                memory[2] = math.trunc(memory[0] / pow(2, x))

        i += 2

    return outs


def getComboOperand(n, memory):

    if n <= 3:
        return n
    elif n <= 6:
        return memory[n - 4]
    else:
        return None


if __name__ == "__main__":
    main()