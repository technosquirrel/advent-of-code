def main():
    
    code = parseInput("input.txt")
    print(run(code)[0])

    for inst in code:
        if inst[0] == "nop":
            inst[0] = "jmp"
            n = run(code)
            if n[1] == True:
                print(n[0])
                return
            else:
                inst[0] = "nop"
        elif inst[0] == "jmp":
            inst[0] = "nop"
            n = run(code)
            if n[1] == True:
                print(n[0])
                return
            else:
                inst[0] = "jmp"


def parseInput(f):

    code = []
    with open(f) as file:
        for line in file:
            line = line.strip().split()
            code.append([line[0], int(line[1])])
    return code


def run(code):

    visited = []
    a = 0
    i = 0

    while i not in visited and i < len(code):
        visited.append(i)
        match code[i][0]:
            case "acc":
                a += code[i][1]
                i += 1
            case "jmp":
                i += code[i][1]
            case "nop":
                i += 1

    if i >= len(code):
        return a, True
    else:
        return a, False


if __name__ == "__main__":
    main()