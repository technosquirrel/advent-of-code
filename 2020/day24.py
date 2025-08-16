import re

DIRS = {
    "ne" : (1, 0, -1),
    "e" : (1, -1, 0),
    "se" : (0, -1, 1),
    "sw" : (-1, 0, 1),
    "w" : (-1, 1, 0),
    "nw" : (0, 1, -1),
}

def main():

    tiles = {(0, 0, 0) : "white"}
    start = (0, 0, 0)
    
    insts = parseInput("input.txt")
    for i in insts:
        tile = findTileCoords(i, start)
        if tile in tiles:
            tiles[tile] = tiles[tile] == "white" and "black" or "white"
        else:
            tiles[tile] = "black"
    
    print(countBlack(tiles))

    # Part 2

    blackTiles = {tile : None for tile in tiles if tiles[tile] == "black"}
    for _ in range(100):
        blackTiles = flipTiles(blackTiles)
    print(len(blackTiles))


def parseInput(f):
    with open(f) as file:
        return [re.findall(r"(se|sw|ne|nw|e|w)", line.strip()) for line in file]


def findTileCoords(line, start):

    coords = [x for x in start]

    for i in line:
        for j in range(3):
            coords[j] += DIRS[i][j]
    
    return tuple(coords)


def countBlack(tiles):
    return len([tiles[tile] for tile in tiles if tiles[tile] == "black"])


def flipTiles(tiles):

    limits = []
    for i in range(3):
        buffer = [x[i] for x in tiles]
        buffer.sort()
        limits.append((buffer[0] - 1, buffer[-1] + 2))

    newTiles = {}
    for i in range(limits[0][0], limits[0][1]):
        for j in range(limits[1][0], limits[1][1]):
            for k in range(limits[2][0], limits[2][1]):
                colour = getColour(tiles, (i, j, k))
                if colour == "black":
                    newTiles[(i, j, k)] = None
    return newTiles


def getColour(tiles, tile):
    
    count = 0

    for d in DIRS:
        c = (tile[0] + DIRS[d][0], tile[1] + DIRS[d][1], tile[2] + DIRS[d][2])
        if c in tiles:
            count += 1

    if tile in tiles:
        if count == 0 or count > 2:
            return "white"
        else:
            return "black"
    else:
        if count == 2:
            return "black"
        else:
            return "white"


if __name__ == "__main__":
    main()