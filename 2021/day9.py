DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main():
    grid = parseInput("input.txt")
    
    risk = 0
    for coord in grid:
        buffer = getAdjacents(coord, grid)
        if all(True if x[1] > grid[coord] else False for x in buffer):
            risk += grid[coord] + 1
    print(risk)

    basins = getBasins(grid)
    basins.sort()
    print(basins[-3] * basins[-2] * basins[-1])


def parseInput(f):
    data = {}
    with open(f) as file:
        for i, line in enumerate(file):
            for j, n in enumerate(line.strip()):
                data[(i, j)] = int(n)
    return data


def getAdjacents(coord, grid):

    adjacents = []
    for d in DIRS:
        try:
            adjacents.append([(coord[0] + d[0], coord[1] + d[1]), grid[(coord[0] + d[0], coord[1] + d[1])]])
        except:
            pass
    return adjacents


def getBasins(grid):

    basins = []
    visited = {}

    for coord in grid:
        if coord in visited or grid[coord] == 9:
            continue
        else:
            basin = 0
            toCheck = [coord]
            while len(toCheck) != 0:
                buffer = []
                for c in toCheck:
                    if c in visited or grid[c] == 9:
                        continue
                    else:
                        buffer += [x[0] for x in getAdjacents(c, grid)]
                        visited[c] = None
                        basin += 1
                toCheck = buffer
        basins.append(basin)

    return basins




if __name__ == "__main__":
    main()