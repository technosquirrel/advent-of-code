import heapq

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    
    maze = parseInput("input.txt")

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "E":
                end = (i, j)

    part1, steps = aStar(start, end, maze, 1)
    print(part1, steps)

    # part2
    turns = (part1 - steps) // 1000
    visited = dijkstra(start, end, maze, 1, steps, turns)
    paths = [[end]]
    
    while True:
        newPaths = []
        for path in paths:
            tmp = visited[path[-1]]["from"]
            for p in tmp:
                if p:
                    newPaths.append(path + [p])
        if not newPaths:
            break
        else:
            paths = newPaths

    part2 = set()
    for path in paths:
        if isValid(path, part1):
            for p in path:
                part2.add(p)

    print(len(part2))




def parseInput(f):
    with open(f) as file:
        return [[x for x in line.strip()] for line in file]


def manhattanDistance(p1, p2):

    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])

    if x == 0 or y == 0:
        return x + y
    else:
        return x + y + 1000
    

def aStar(start, end, maze, dir):
    
    location = (manhattanDistance(start, end), manhattanDistance(start, end), 0, dir, start, 0)
    locations = []
    heapq.heappush(locations, location)
    visited = {}


    while len(locations) > 0:

        location = heapq.heappop(locations)

        if location[4] == end:
            return location[2], location[5]
        elif location[4] in visited:
            continue
        else:
            visited[location[4]] = location[2]
            x = (location[4][0] + DIRS[location[3]][0], location[4][1] + DIRS[location[3]][1])
            if maze[x[0]][x[1]] != "#" and x not in visited:
                g = location[2] + 1
                h = manhattanDistance(x, end)
                heapq.heappush(locations, (g + h, h, g, location[3], x, location[5] + 1))
            ds = [(location[3] - 1) % 4, (location[3] + 1) % 4]
            for d in ds:
                x = (location[4][0] + DIRS[d][0], location[4][1] + DIRS[d][1])
                if maze[x[0]][x[1]] != "#" and x not in visited:
                    g = location[2] + 1001
                    h = manhattanDistance(x, end)
                    heapq.heappush(locations, (g + h, h, g, d, x, location[5] + 1))


def dijkstra(start, end, maze, dir, steps, turns):
    
    # cost, steps, turns, coord, direction, previous
    location = (0, 0, 0, start, dir, None)
    locations = []
    heapq.heappush(locations, location)
    visited = {}

    while len(locations) > 0:
        location = heapq.heappop(locations)
        
        if location[3] == end:
            if location[0] > steps + turns * 1000:
                return visited
            else:
                try:
                    visited[location[3]]["from"].append(location[5])
                except:
                    visited[location[3]] = {"cost" : location[0], "steps" : location[1], "turns" : location[2], "from" : [location[5]]}
        elif location[3] in visited:
            if location[1] == visited[location[3]]["steps"]:
                visited[location[3]]["from"].append(location[5])
            else:
                continue
        else:
            visited[location[3]] = {"cost" : location[0], "steps" : location[1], "turns" : location[2], "from" : [location[5]]}
            x = (location[3][0] + DIRS[location[4]][0], location[3][1] + DIRS[location[4]][1])
            if maze[x[0]][x[1]] != "#" and (x not in visited or location[1] + 1 == visited[x]["steps"]):
                heapq.heappush(locations, (location[0] + 1, location[1] + 1, location[2], x, location[4], location[3]))
            ds = [(location[4] + 1) % 4, (location[4] - 1) % 4]
            for d in ds:
                x = (location[3][0] + DIRS[d][0], location[3][1] + DIRS[d][1])
                if maze[x[0]][x[1]] != "#" and (x not in visited or location[1] + 1 == visited[x]["steps"]):
                    heapq.heappush(locations, (location[0] + 1001, location[1] + 1, location[2] + 1, x, d, location[3]))

    return visited


def isValid(path, minCost):

    path.reverse()
    d = 1
    cost = 0

    for i in range(0, len(path) - 1):
        cost += 1
        dir = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
        if DIRS.index(dir) != d:
            cost += 1000
            d = DIRS.index(dir)

    if cost == minCost:
        return True
    else:
        return False


if __name__ == "__main__":
    main()