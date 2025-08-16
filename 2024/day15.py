dirs = {
    "<" : (0, -1),
    "^" : (-1, 0),
    ">" : (0, 1),
    "v" : (1, 0)
}

def main():
    
    grid, instructions = parseInput("input.txt")
    robot = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                robot = [i, j]
                break

    for move in instructions:
        x = [robot[0], robot[1]]
        while grid[x[0]][x[1]] != "." and grid[x[0]][x[1]] != "#":
            for i in range(2):
                x[i] += dirs[move][i]
        if grid[x[0]][x[1]] == ".":
            y = [x[0], x[1]]
            while x != robot:
                for i in range(2):
                    y[i] -= dirs[move][i]
                grid[x[0]][x[1]], grid[y[0]][y[1]] = grid[y[0]][y[1]], grid[x[0]][x[1]]
                x = [y[0], y[1]]
            for i in range(2):
                robot[i] += dirs[move][i]

    part1 = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                part1 += i * 100 + j
    print(part1)


    #part2

    grid, instructions = parseInput2("input.txt")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                robot = [i, j]
                break
            
    for move in instructions:
        x = [robot[0], robot[1]]
        if move == "<" or move == ">":
            while grid[x[0]][x[1]] != "." and grid[x[0]][x[1]] != "#":
                for i in range(2):
                    x[i] += dirs[move][i]
            if grid[x[0]][x[1]] == ".":
                y = [x[0], x[1]]
                while x != robot:
                    for i in range(2):
                        y[i] -= dirs[move][i]
                    grid[x[0]][x[1]], grid[y[0]][y[1]] = grid[y[0]][y[1]], grid[x[0]][x[1]]
                    x = [y[0], y[1]]
                for i in range(2):
                    robot[i] += dirs[move][i]
        else:
            locations = [x]
            if tryMove(locations, grid, move):
                for i in range(2):
                    robot[i] += dirs[move][i]

    part2 = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                part2 += i * 100 + j
    print(part2)
         

def parseInput(f):

    grid = []
    instructions = []

    with open(f) as file:
        for line in file:
            line = line.strip()
            if line:
                if line.startswith("#"):
                    grid.append([x for x in line])
                else:
                    instructions += [x for x in line]

    return grid, instructions


def parseInput2(f):

    subs = {
        "." : [".", "."],
        "#" : ["#", "#"],
        "@" : ["@", "."],
        "O" : ["[", "]"],
    }

    grid = []
    instructions = []

    with open(f) as file:
        for line in file:
            line = line.strip()
            if line:
                if line.startswith("#"):
                    buffer = []
                    for c in line:
                        buffer += subs[c]
                    grid.append(buffer)
                else:
                    instructions += [x for x in line]

    return grid, instructions


def tryMove(coords, grid, move):

    buffer = [grid[x[0]][x[1]] for x in coords]

    if all([True if x == "." else False for x in buffer]):
        return True
    elif "#" in buffer:
        return False
    else:
        newCoords = []
        for i, v in enumerate(buffer):
            if v != ".":
                newCoords.append([coords[i][0] + dirs[move][0], coords[i][1] + dirs[move][1]])
        toAdd = []
        for coord in newCoords:
            if grid[coord[0]][coord[1]] == "[" and [coord[0], coord[1] + 1] not in newCoords:
                toAdd.append([coord[0], coord[1] + 1])
            elif grid[coord[0]][coord[1]] == "]" and [coord[0], coord[1] - 1] not in newCoords:
                toAdd.append([coord[0], coord[1] - 1])
        newCoords += toAdd
        if tryMove(newCoords, grid, move):
            for x in newCoords:
                y = [x[0] - dirs[move][0], x[1] - dirs[move][1]]
                if y in coords:
                    grid[x[0]][x[1]], grid[y[0]][y[1]] = grid[y[0]][y[1]], grid[x[0]][x[1]]
            return True
        else:
            return False
        


if __name__ == "__main__":
    main()