import heapq

def main():
    
    blocks = parseInput("input.txt")
    
    start = (1, 1)
    end = (71, 71)
    grid = [["." for _ in range(71)] for _ in range(71)]

    for i in range(1024):
        grid[blocks[i][0]][blocks[i][1]] = "#"
    
    for i, line in enumerate(grid):
        grid[i] = ["#"] + line + ["#"]
    grid.insert(0, ["#" for _ in grid[0]])
    grid.append(["#" for _ in grid[0]])

    visited = aStar(start, end, grid)
    print(visited[end][0])

    path = reconstructPath(visited, end)

    i = 1024
    while True:
        grid[blocks[i][0] + 1][blocks[i][1] + 1] = "#"
        if (blocks[i][0] + 1, blocks[i][1] + 1) in path:
            visited = aStar(start, end, grid)
            if not visited:
                print(blocks[i][::-1])
                break
            else:
                path = reconstructPath(visited, end)
        i += 1

def parseInput(f):
    with open(f) as file:
        return [tuple([int(x) for x in line.strip().split(",")][::-1]) for line in file]
    

def aStar(start, end, maze):
    
    location = (manhattanDistance(start, end), manhattanDistance(start, end), 0, start, None)
    locations = []
    heapq.heappush(locations, location)
    visited = {}
    
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while len(locations) > 0:
        location = heapq.heappop(locations)
        if location[3] == end:
            visited[location[3]] = [location[2], location[4]]
            return visited
        elif location[3] in visited:
            continue
        else:
            visited[location[3]] = [location[2], location[4]]
            for dir in dirs:
                x = (location[3][0] + dir[0], location[3][1] + dir[1])
                if x not in visited and maze[x[0]][x[1]] != "#":
                    g = location[2] + 1
                    h = manhattanDistance(x, end)
                    heapq.heappush(locations, (g + h, h, g, x, location[3]))

    return False


def manhattanDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def reconstructPath(visited, end):
    path = {end : True}
    location = end
    while visited[location][1]:
        location = visited[location][1]
        path[location] = True
    return path


if __name__ == "__main__":
    main()