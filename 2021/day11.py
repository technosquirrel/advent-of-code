def main():

    data = parseInput("input.txt")

    flashes = 0
    i = 0
    while True:
        coords = [x for x in data]
        while len(coords) > 0:
            c = coords.pop(0)
            if data[c] == -1:
                continue
            data[c] += 1
            if data[c] > 9:
                flashes += 1
                data[c] = -1
                coords += getAdjacents(c, data)

        count = 0
        for c in data:
            if data[c] == -1:
                data[c] = 0
                count += 1
        
        i += 1
        if i == 100:
            print(flashes)

        if count == len(data):
            print(i)
            break


def parseInput(f):

    data = {}
    with open(f) as file:
        for i, line in enumerate(file):
            for j, n in enumerate(line.strip()):
                data[(i, j)] = int(n)
    return data


def getAdjacents(coord, grid):

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    adjacents = []

    for d in dirs:
        c = (coord[0] + d[0], coord[1] + d[1])
        if c in grid and grid[c] != -1:
            adjacents.append(c)

    return adjacents
    

if __name__ == "__main__":
    main()