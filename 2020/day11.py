MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def main():
    
    data = parseInput("input.txt")
    grid = [[x for x in line] for line in data]

    while True:
        newGrid = simulateMoves(grid)
        if grid == newGrid:
            count = 0
            for line in grid:
                count += line.count("#")
            print(count)
            break
        grid = newGrid

    grid = [[x for x in line] for line in data]
    while True:
        newGrid = simulateMoves(grid, True)
        if grid == newGrid:
            count = 0
            for line in grid:
                count += line.count("#")
            print(count)
            break
        grid = newGrid


def parseInput(f):
    grid = []
    with open(f) as file:
        for line in file:
            grid.append(["."] + [x for x in line.strip()] + ["."])
    grid.insert(0, ["." for _ in grid[0]])
    grid.append(["." for _ in grid[0]])
    return grid


def simulateMoves(grid, part2=False):

    newGrid = [[x for x in line] for line in grid]
    n = 5 if part2 else 4
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] != ".":
                if not part2:
                    adjacents = getAdjacents(grid, i, j)
                else:
                    adjacents = getAdjacents2(grid, i, j)
                if grid[i][j] == "L" and "#" not in adjacents:
                    newGrid[i][j] = "#"
                elif grid[i][j] == "#" and adjacents.count("#") >= n:
                    newGrid[i][j] = "L"

    return newGrid


def getAdjacents(grid, i, j):

    adjacents = []
    for move in MOVES:
        adjacents.append(grid[i + move[0]][j + move[1]])
    return adjacents


def getAdjacents2(grid, i, j):
    
    adjacents = []

    for move in MOVES:
        mult = 1
        while True:
            x = i + move[0] * mult
            y = j + move[1] * mult
            if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
                adjacents.append(".")
                break
            elif grid[x][y] != ".":
                adjacents.append(grid[x][y])
                break
            else:
                mult += 1

    return adjacents

if __name__ == "__main__":
    main()