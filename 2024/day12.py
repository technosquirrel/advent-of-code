def main():
    
    grid = parseInput("input.txt")
    n = 0

    part1 = []
    checked = {}

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[1]) - 1):
            if grid[i][j] not in checked:
                a = floodFill(grid, [i, j], [grid[i][j]], str(n).zfill(3))
                part1.append(list(a))
                checked[str(n).zfill(3)] = True
                n += 1

    checked = {}
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[1]) - 1):
            if grid[i][j] not in checked:
                p, p2 = findPerimeter(grid, [i, j], part1[int(grid[i][j])][1], part1[int(grid[i][j])][2])
                checked[grid[i][j]] = True
                part1[int(grid[i][j])].insert(1, p)
                part1[int(grid[i][j])].insert(2, p2)

    print(sum(x[0] * x[1] for x in part1))
    print(sum(x[0] * x[2] for x in part1))


def parseInput(f):
    with open(f) as file:
        grid = [["."] + [x for x in line.strip()] + ["."] for line in file]
        grid.insert(0, ["." for _ in grid[0]])
        grid.append(["." for _ in grid[0]])
    return grid


def floodFill(grid, position, match, replacement, diagonal=False):

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if diagonal:
        dirs += [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    minCoord = [position[0], position[1]]
    maxCoord = [position[0], position[1]]
    a = 1
    
    locations = [position]
    grid[position[0]][position[1]] = replacement

    while len(locations) > 0:
        newLocations = set()
        for location in locations:
            for i in range(2):
                if location[i] < minCoord[i]:
                    minCoord[i] = location[i]
                if location[i] > maxCoord[i]:
                    maxCoord[i] = location[i]
            for dir in dirs:
                x = (location[0] + dir[0], location[1] + dir[1])
                if (match[0] == "^" and (grid[x[0]][x[1]] not in match)) or (match[0] != "^" and (grid[x[0]][x[1]] in match)):
                    grid[x[0]][x[1]] = replacement
                    a += 1
                    newLocations.add(x)
        locations = newLocations

    return a, minCoord, maxCoord, position


def findPerimeter(grid, position, minCoord, maxCoord):
    
    dirs = [[(-1, 0), (0, 1), (-1, -1)], [(0, 1), (1, 0), (-1, 1)], [(1, 0), (0, -1), (1, 1)], [(0, -1), (-1, 0), (1, -1)]]

    gridReduced = [["."] + grid[i][minCoord[1] : maxCoord[1] + 1] + ["."] for i in range(minCoord[0], maxCoord[0] + 1)]
    gridReduced.insert(0, ["." for _ in gridReduced[0]])
    gridReduced.append(["." for _ in gridReduced[0]])

    start = [position[0] - minCoord[0] + 1, position[1] - minCoord[1] + 1]
    n = gridReduced[start[0]][start[1]]
    r = "R"

    areas = []

    for i in range(1, len(gridReduced) - 1):
        for j in range(1, len(gridReduced[0]) - 1):
            if gridReduced[i][j] != n and gridReduced[i][j] != r:
                areas.append(floodFill(gridReduced, [i, j], ["^", ".", n, r], r, True))

    p = 0
    p2 = 0
    location = [start[0], start[1]]
    index = 0

    while True:
        x = [location[0] + dirs[index][0][0], location[1] + dirs[index][0][1]]
        y = [location[0] + dirs[index][1][0], location[1] + dirs[index][1][1]]
        if gridReduced[x[0]][x[1]] == n:
            location = x
            index = (index - 1) % 4
            p2 += 1
        elif gridReduced[y[0]][y[1]] == n:
            p += 1
            location = y
        else:
            p += 1
            index = (index + 1) % 4
            p2 += 1
        if location == start and index == 0:
            break 


    for area in areas:
        if area[1][0] > 1 and area[1][1] > 1 and area[2][0] < len(gridReduced) - 2 and area[2][1] < len(gridReduced[0]) - 2:
            location = [x - 1 for x in area[3]]
            index = 2
            start = [location[0], location[1]]
            while True:
                x = [location[0] + dirs[index][0][0], location[1] + dirs[index][0][1]]
                y = [location[0] + dirs[index][1][0], location[1] + dirs[index][1][1]]

                if gridReduced[x[0]][x[1]] == n:
                    location = x
                    index = (index - 1) % 4
                    p2 += 1
                elif gridReduced[y[0]][y[1]] == n:
                    p += 1
                    location = y
                else:
                    p += 1
                    index = (index + 1) % 4
                    p2 += 1
                if location == start and index == 2:
                    break

    return p, p2


if __name__ == "__main__":
    main()