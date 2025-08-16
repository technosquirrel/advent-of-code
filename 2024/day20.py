import time
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    
    s = time.time()
    grid = parseInput("input.txt")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    steps = countSteps(start, end, grid)
    raceTime = steps[end]

    cheats = {}
    cheatCount = {}
    
    for location in steps:
        for dir in DIRS:
            x = (location[0] + dir[0], location[1] + dir[1])
            if x not in cheats and grid[x[0]][x[1]] == "#":
                try:
                    y = (x[0] + dir[0], x[1] + dir[1])
                    if grid[y[0]][y[1]] in (".", "E"):
                        t = raceTime - (steps[location] + raceTime - steps[y] + 2)
                        if t > 0:
                            try:
                                cheatCount[t] += 1
                            except:
                                cheatCount[t] = 1
                            cheats[x] = None
                except:
                    pass

    print(sum([cheatCount[x] for x in cheatCount if x >= 100]))

    locationsList = [x for x in steps]
    part2 = 0

    for i, location in enumerate(locationsList):
        for j in range(i + 101, len(locationsList)):
            n = manhattanDistance(location, locationsList[j])
            if n <= 20:
                t = raceTime - (steps[location] + manhattanDistance(location, locationsList[j]) + raceTime - steps[locationsList[j]])
                if t >= 100:
                    part2 += 1


    print(part2)
    print(time.time() - s)


def parseInput(f):
    with open(f) as file:
        return [[x for x in line.strip()] for line in file]


def countSteps(start, end, grid):

    steps = 0
    visited = {start : 0} 
    location = start

    while location != end:
        for dir in DIRS:
            x = (location[0] + dir[0], location[1] + dir[1])
            if grid[x[0]][x[1]] != "#" and x not in visited:
                location = x
                steps += 1
                visited[location] = steps
                break

    return visited


def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


if __name__ == "__main__":
    main()