import numpy as np
import math

def main():

    tiles = parseInput("input.txt")

    for id in tiles:
        tiles[id]["edges"] = getEdges(tiles[id]["tile"])
        tiles[id]["connections"] = set()

    
    corners = []
    for id in tiles:
        for dir in tiles[id]["edges"]:
            edge = tiles[id]["edges"][dir]
            for i in tiles:
                if i == id:
                    continue
                for d in tiles[i]["edges"]:
                    if tiles[i]["edges"][d] == edge[::-1]:
                        tiles[id]["connections"].add(i)
                    elif tiles[i]["edges"][d] == edge:
                        tiles[i] = flipTile(tiles[i])
                        tiles[id]["connections"].add(i)
        if len(tiles[id]["connections"]) == 2:
            corners.append(id)

    print(corners[0] * corners[1] * corners[2] * corners[3])


    # Part 2
    cxs = [x for x in tiles[corners[0]]["connections"]]

    tileW = len(tiles[corners[0]]["tile"]) - 2
    puzzleW = int(math.sqrt(len(tiles)))
    grid = np.array([["." for _ in range(puzzleW * tileW)] for _ in range(puzzleW * tileW)])

    while True:
        dirs = []
        for c in cxs:
            for d in tiles[c]["edges"]:
                for dir in tiles[corners[0]]["edges"]:
                    if tiles[c]["edges"][d] == tiles[corners[0]]["edges"][dir][::-1]:
                        dirs.append(dir)
        if "down" in dirs and "right" in dirs:
            break
        else:
            tiles[corners[0]] = rotateTile(tiles[corners[0]])

    tile = removeEdges(tiles[corners[0]]["tile"])
    updateGrid(tile, grid, 0, 0)
    
    left = tiles[corners[0]]
    up = tiles[corners[0]]

    for i in range(puzzleW):
        for j in range(puzzleW):
            if j == 5:
                breakpoint
            if i == 0 and j == 0:
                continue
            elif j == 0:
                newTileId = 0
                edge = up["edges"]["down"][::-1]
                for id in up["connections"]:
                    for dir in tiles[id]["edges"]:
                        if tiles[id]["edges"][dir] == edge:
                            newTileId = id
                            break
                        elif tiles[id]["edges"][dir] == edge[::-1]:
                            newTileId = id
                            tiles[id] = flipTile(tiles[id])
                            break
                while tiles[newTileId]["edges"]["up"] != edge:
                    tiles[newTileId] = rotateTile(tiles[newTileId])
                newTile = removeEdges(tiles[newTileId]["tile"])
                updateGrid(newTile, grid, i * tileW, j * tileW)
                up = tiles[newTileId]
                left = tiles[newTileId]
            else:
                newTileId = 0
                edge = left["edges"]["right"][::-1]
                for id in left["connections"]:
                    for dir in tiles[id]["edges"]:
                        if tiles[id]["edges"][dir] == edge:
                            newTileId = id
                            break
                        elif tiles[id]["edges"][dir] == edge[::-1]:
                            newTileId = id
                            tiles[id] = flipTile(tiles[id])
                            break
                while tiles[newTileId]["edges"]["left"] != edge:
                    tiles[newTileId] = rotateTile(tiles[newTileId])
                newTile = removeEdges(tiles[newTileId]["tile"])
                updateGrid(newTile, grid, i * tileW, j * tileW)
                left = tiles[newTileId]


    seaMonster = parseMonster("monster.txt")
    w = len(seaMonster[0])
    h = len(seaMonster)

    r = 0

    while True:
        seaMonsters = 0
        for i in range(len(grid) - h):
            for j in range(len(grid) - w):
                if isMonster(grid, i, j, seaMonster):
                    seaMonsters += 1
        if seaMonsters > 0:
            break
        else:
            if r == 3:
                r = 0
                grid = np.fliplr(grid)
            else:
                grid = np.rot90(grid)
                r += 1

    print(sum([[x for x in line].count("#") for line in grid]))
    


def parseInput(f):

    tiles = {}

    with open(f) as file:
        for line in file:
            line = line.strip()
            if not line:
                tiles[id] = {"tile" : np.array(tile)}
            elif line.startswith("Tile"):
                id = int(line[5:-1])
                tile = []
            else:
                tile.append([x for x in line])

    tiles[id] = {"tile" : np.array(tile)}

    return tiles


def getEdges(tile):

    edges = {}

    edges["up"] = "".join([str(x) for x in tile[0]])
    edges["right"] = "".join([str(line[-1]) for line in tile])
    edges["down"] = "".join([str(x) for x in tile[-1]][::-1])
    edges["left"] = "".join([str(line[0]) for line in tile][::-1])

    return edges


def flipTile(data):

    tmp = {}
    tmp["tile"] = np.fliplr(data["tile"])
    tmp["edges"] = getEdges(tmp["tile"])
    tmp["connections"] = data["connections"]
    return tmp


def rotateTile(data):

    tmp = {}
    tmp["tile"] = np.rot90(data["tile"], axes=(1,0))
    tmp["edges"] = getEdges(tmp["tile"])
    tmp["connections"] = data["connections"]
    return tmp


def removeEdges(tile):
    return np.array([[x for x in line[1:-1]] for line in tile[1:-1]])


def updateGrid(tile, grid, x, y):

    for i in range(len(tile)):
        for j in range(len(tile)):
            grid[x + i][j + y] = tile[i][j]


def parseMonster(f):
    with open(f) as file:
        return [[x for x in line[:-1]] for line in file]


def isMonster(grid, i, j, monster):
    for x in range(len(monster)):
        for y in range(len(monster[0])):
            if monster[x][y] == "#":
                if grid[i + x][j + y] != "#":
                    return False
    
    for x in range(len(monster)):
        for y in range(len(monster[0])):
            if monster[x][y] == "#":
                grid[i + x][j + y] = "O"
    return True


if __name__ == "__main__":
    main()