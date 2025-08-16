import math

def main():

    passes = parseInput("input.txt")

    part1 = 0
    lowest = 100000
    ids = {}
    for p in passes:
        x = getSeatID(p)
        ids[x] = True
        if x > part1:
            part1 = x
        if x < lowest:
            lowest = x
    print(part1)

    for i in range(lowest, part1 + 1):
        if i not in ids:
            print(i)
            return


def parseInput(f):
    with open(f) as file:
        return [[x for x in line.strip()] for line in file]
    

def getSeatID(p):

    rows = [0, 127]
    columns = [0, 7]

    for c in p:
        if c == "F":
            rows[1] = rows[0] + (rows[1] - rows[0]) // 2
        elif c == "B":
            rows[0] += math.ceil((rows[1] - rows[0]) / 2)
        elif c == "L":
            columns[1] = columns[0] + (columns[1] - columns[0]) // 2
        elif c == "R":
            columns[0] += math.ceil((columns[1] - columns[0]) / 2)
        else:
            raise ValueError

    return rows[0] * 8 + columns[0]


if __name__ == "__main__":
    main()