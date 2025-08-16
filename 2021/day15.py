import heapq
import time
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def main():

    s = time.time()
    data = parseInput("input.txt")
    grid = makeGrid(data)

    print(aStar(grid, (0, 0), (len(data) - 1, len(data[0]) - 1)))

    newGrid = {}
    for i in range(5):
        for j in range(5):
            for x in range(len(data)):
                for y in range(len(data[0])):
                    n = data[x][y] + i + j
                    if n > 9:
                        n = n - 9
                    newGrid[(x + len(data) * i, y + len(data[0]) * j)] = n

    print(aStar(newGrid, (0, 0),( len(data) * 5 - 1, len(data[0]) * 5 - 1)))
    print(time.time() - s)


def parseInput(f):
    with open(f) as file:
        return[[int(x) for x in line.strip()] for line in file]


def makeGrid(data):

    grid = {}

    for i in range(len(data)):
        for j in range(len(data[0])):
            grid[(i, j)] = data[i][j]

    return grid


def aStar(grid, start, end):

    locations = [(manhattanDistance(start, end), manhattanDistance(start, end), 0, start)]
    heapq.heapify(locations)

    visited = {}
    
    while len(locations) > 0:
        
        l = heapq.heappop(locations)

        if l[3] == end:
            return l[2]
        elif l[3] in visited:
            continue
        visited[l[3]] = None
        
        adjs = getAdjacents(l[3], grid)
        for a in adjs:
            if a in visited:
                continue
            heapq.heappush(locations, (manhattanDistance(a, end) + l[2] + grid[a], manhattanDistance(a, end), l[2] + grid[a], a))


def manhattanDistance(c, end):
    return abs(c[0] - end[0]) + abs(c[1] - end[1])


def getAdjacents(c, grid):
    adjacents = []
    for d in DIRS:
        n = (d[0] + c[0], d[1] + c[1])
        if n in grid:
            adjacents.append(n)
    return adjacents


if __name__ == "__main__":
    main()