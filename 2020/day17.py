from itertools import product
import time

DIRS = list(product((0, 1, -1), repeat=3))
DIRS.remove((0, 0, 0))
DIRS2 = list(product((0, 1, -1), repeat=4))
DIRS2.remove((0, 0, 0, 0))


def main():
    
    start = time.time()
    data = parseInput("input.txt")
    coords = {x : None for x in data}
    
    for _ in range(6):
        coords = runCycle(coords)

    print(len(coords))

    coords2 = {(x[0], x[1], 0, 0) : None for x in data}

    for _ in range(6):
        coords2 = runCycle2(coords2)
    
    print(len(coords2))
    print(time.time() - start)


def parseInput(f):

    buffer = {}

    with open(f) as file:
        for i, line in enumerate(file):
            line = [x for x in line.strip()]
            for j, n in enumerate(line):
                if n == "#":
                    buffer[(i, j, 0)] = None

    return buffer


def runCycle(coords):

    limits = []

    for i in range(3):
        buffer = [x[i] for x in coords]
        buffer.sort()
        limits.append((buffer[0] - 1, buffer[-1] + 2))

    
    newCoords = {}

    for i in range(limits[0][0], limits[0][1]):
        for j in range(limits[1][0], limits[1][1]):
            for k in range(limits[2][0], limits[2][1]):
                x = countAdjacents(i, j, k, coords)
                if (i, j, k) in coords:
                    if x == 2 or x == 3:
                        newCoords[(i, j, k)] = None
                elif x == 3:
                    newCoords[(i, j, k)] = None

    return newCoords


def countAdjacents(i, j, k, coords):

    count = 0

    for dir in DIRS:
        c = (i + dir[0], j + dir[1], k + dir[2])
        if c in coords:
            count += 1

    return count


def runCycle2(coords):
    
    limits = []

    for i in range(4):
        buffer = [x[i] for x in coords]
        buffer.sort()
        limits.append((buffer[0] - 1, buffer[-1] + 2))

    
    newCoords = {}

    for i in range(limits[0][0], limits[0][1]):
        for j in range(limits[1][0], limits[1][1]):
            for k in range(limits[2][0], limits[2][1]):
                for l in range(limits[3][0], limits[3][1]):
                    x = countAdjacents2(i, j, k, l, coords)
                    if (i, j, k, l) in coords:
                        if x == 2 or x == 3:
                            newCoords[(i, j, k, l)] = None
                    elif x == 3:
                        newCoords[(i, j, k, l)] = None

    return newCoords


def countAdjacents2(i, j, k, l, coords):

    count = 0

    for dir in DIRS2:
        c = (i + dir[0], j + dir[1], k + dir[2], l + dir[3])
        if c in coords:
            count += 1

    return count


if __name__ == "__main__":
    main()