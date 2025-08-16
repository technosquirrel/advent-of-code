def main():
    
    locks, keys = parseInput("input.txt")

    part1 = 0

    for lock in locks:
        for key in keys:
            if all(True if x - (5 - y) <= 0 else False for x, y in zip(lock, key)):
                part1 += 1

    print(part1)


def parseInput(f):

    locks = []
    keys = []

    with open(f) as file:
        buffer = []
        for line in file:
            line = line.strip()
            if not line:
                seq = []
                for j in range(len(buffer[0])):
                    col = 0
                    for i in range(len(buffer)):
                        if buffer[i][j] == "#":
                            col += 1
                    seq.append(col - 1)
                if buffer[0][0] == "#":
                    locks.append(seq)
                else:
                    keys.append(seq)
                buffer = []
            else:
                buffer.append([x for x in line])

    return locks, keys


if __name__ == "__main__":
    main()