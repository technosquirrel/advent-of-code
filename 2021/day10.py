def main():
    
    data = parseInput("input.txt")

    scores = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}

    part1 = 0
    part2 = []
    for line in data:
        x = isCorrupt(line)
        if x[0]:
            part1 += scores[x[1]]
        else:
            while True:
                if any(True if m in scores else False for m in [n for n in x[1]]):
                    x = isCorrupt(x[1])
                else:
                    break
            braces = getClosingBraces(x[1])
            part2.append(scoreBraces(braces))

    print(part1)
    part2.sort()
    print(part2[len(part2) // 2])


def parseInput(f):
    with open(f) as file:
        return [line.strip() for line in file]


def isCorrupt(line):

    braces = {"(" : ")", "{": "}", "<" : ">", "[" : "]"}
    l = line

    while True:
        if len(l) == 0:
            return [False, l]
        elif all(True if x in braces else False for x in l):
            return [False, l]
        elif len(l) == 1:
            return [True, l]
        elif l[1] == braces[l[0]]:
            return [False, l[2:]]
        elif l[1] not in braces:
            return [True, l[1]]
        else:
            x = isCorrupt(l[1:])
            if x[0]:
                return [True, x[1]]
            else:
                l = l[0] + x[1]


def getClosingBraces(x):

    braces = {"(" : ")", "{": "}", "<" : ">", "[" : "]"}
    buffer = []
    for i in range(len(x) - 1, -1, -1):
        buffer.append(braces[x[i]])
    return buffer


def scoreBraces(braces):

    scores = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
    score = 0

    for x in braces:
        score = (score * 5) + scores[x]

    return score


if __name__ == "__main__":
    main()