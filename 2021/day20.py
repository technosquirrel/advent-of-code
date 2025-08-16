def main():
    
    key, coords = parseInput("input.txt")
    
    for i in range(50):
        coords = expandImage(key, coords, i)

    print(len(coords))


def parseInput(f):

    with open(f) as file:

        key = file.readline().strip()
        file.readline()

        img = []
        for line in file:
            img.append([x for x in line.strip()])
    
        coords = {}
        for i in range(len(img)):
            for j in range(len(img[i])):
                if img[i][j] == "#":
                    coords[(i, j)] = None

    return key, coords


def expandImage(key, coords, n):

    tmp = [[x[0] for x in coords], [x[1] for x in coords]]
    constraints = (min(tmp[0]), max(tmp[0]), min(tmp[1]), max(tmp[1]))

    newCoords = {}
    filler = "."
    if key[0] == "#" and n % 2 == 1:
        filler = "#"

    for i in range(constraints[0] - 1, constraints[1] + 2):
        for j in range(constraints[2] - 1, constraints[3] + 2):
            n = getValue((i, j), coords, constraints, filler)
            if key[n] == "#":
                newCoords[(i, j)] = None

    return newCoords


def getValue(c, coords, constraints, filler):

    x = ""

    for i in range(c[0] - 1, c[0] + 2):
        for j in range(c[1] - 1, c[1] + 2):
            if (i, j) in coords:
                x += "1"
            elif filler == "#" and (i < constraints[0] or i > constraints[1] or j < constraints[2] or j > constraints[3]):
                x += "1"
            else:
                x += "0"

    return int(x, 2)



if __name__ == "__main__":
    main()