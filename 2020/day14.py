from itertools import product

def main():
    
    data = parseInput("input.txt")

    mem = {}
    mask = ""

    for line in data:
        if line[0] == "mask":
            mask = line[1]
        else:
            n = format(line[1], "b").zfill(36)
            mem[line[0]] = "".join([x if y == "X" else y for x, y in zip(n, mask)])
    
    part1 = 0
    for k in mem:
        part1 += int(mem[k], 2)
    print(part1)

    # Part 2

    mem2 = {}
    for line in data:
        if line[0] == "mask":
            mask = line[1]
        else:
            ads = getAddresses(line[0], mask)
            for ad in ads:
                mem2[ad] = line[1]
    part2 = 0
    for k in mem2:
        part2 += mem2[k]
    print(part2)


def parseInput(f):

    buffer = []

    with open(f) as file:
        for line in file:
            line = line.strip().split(" = ")
            if line[0] == "mask":
                buffer.append(line)
            else:
                buffer.append([int(line[0][4:-1]), int(line[1])])

    return buffer


def getAddresses(n, mask):

    n = format(n, "b").zfill(36)
    n = [x if y == "0" else y for x, y in zip(n, mask)]
    opts = product(["0", "1"], repeat=n.count("X"))

    ads = []
    for opt in opts:
        i = 0
        cpy = [x for x in n]
        for j, c in enumerate(cpy):
            if c == "X":
                cpy[j] = opt[i]
                i += 1
        ads.append("".join(cpy))

    return ads


if __name__ == "__main__":
    main()