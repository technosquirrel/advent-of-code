import time

def main():
    
    start = time.time()
    map = parseInput("input.txt")

    part1 = 0
    part2 = 0
    for i, line in enumerate(map):
        for j, x in enumerate(line):
            if x == 0:
                part1 += findTrails(map, (i, j))
                part2 += findDistinctTrails(map, (i, j))
    print(part1, part2)

    print(time.time() - start)


def parseInput(f):

    map = []
    with open(f) as file:
        for line in file:
            map.append([-1] + [int(x) for x in line.strip()] + [-1])
    map.insert(0, [-1 for _ in map[0]])
    map.append([-1 for _ in map[0]])

    return map


def findTrails(map, pos):

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    currentPositions = [pos]

    for i in range(1, 10):
        newPositions = set()
        for position in currentPositions:
            for j in range(4):
                temp = (position[0] + dirs[j][0], position[1] + dirs[j][1])
                if map[temp[0]][temp[1]] == i:
                    newPositions.add(temp)
        currentPositions = newPositions

    return len(currentPositions)


def findDistinctTrails(map, pos):

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    currentPositions = {pos : 1}

    for i in range(1, 10):
        newPositions = {}
        for position in currentPositions:
            for j in range(4):
                temp = (position[0] + dirs[j][0], position[1] + dirs[j][1])
                if map[temp[0]][temp[1]] == i:
                    try:
                        newPositions[temp] += currentPositions[position]
                    except:
                        newPositions[temp] = currentPositions[position]
        currentPositions = newPositions

    return sum(currentPositions.values())



if __name__ == "__main__":
    main()