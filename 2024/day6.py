import time

def main():
    
    s = time.time()
    grid = parseInput("input.txt")
    
    coords = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                start = (i, j)
            coords[(i, j)] = 1 if grid[i][j] == "#" else 0
    
    guard = (start[0], start[1])
    visited = {guard : ["U"]}
    dir = "U"
    dirs = {"U" : (-1, 0), "D" : (1, 0), "L" : (0, -1), "R" : (0, 1)}
    dirsOrder = ["U", "R", "D", "L"]
    while True:
        temp = (guard[0] + dirs[dir][0], guard[1] + dirs[dir][1])
        if temp in coords:
            if coords[temp] == 1:
                dir = dirsOrder[(dirsOrder.index(dir) + 1) % 4]
            else:
                if temp in visited:
                    visited[temp].append(dir)
                else:
                    visited[temp] = [dir]
                guard = temp
        else:
            break
    
    print(len(visited))
    print(time.time() - s)

    obstacles = 0
    guard = (start[0], start[1])
    dir = "U"
    visited = {guard : [dir]}

    while True:
        temp = (guard[0] + dirs[dir][0], guard[1] + dirs[dir][1])
        if temp in coords:
            if coords[temp] == 1:
                dir = dirsOrder[(dirsOrder.index(dir) + 1) % 4]
            else:
                if temp in visited:
                    visited[temp].append(dir)
                else:
                    # Insert obstacle and test for cycles
                    obstacle = (guard[0] + dirs[dir][0], guard[1] + dirs[dir][1])
                    coords[obstacle] = 1
                    testGuard = (guard[0], guard[1])
                    testDir = dirsOrder[(dirsOrder.index(dir) + 1) % 4]
                    testVisited = {testGuard : [testDir]}
                    while True:
                        tempTest = (testGuard[0] + dirs[testDir][0], testGuard[1] + dirs[testDir][1])
                        if tempTest in coords:
                            if tempTest in testVisited and testDir in testVisited[tempTest]:
                                obstacles += 1
                                break
                            elif tempTest in visited and testDir in visited[tempTest]:
                                obstacles += 1
                                break
                            elif coords[tempTest] == 1:
                                testDir = dirsOrder[(dirsOrder.index(testDir) + 1) % 4]
                            else:
                                if tempTest in testVisited:
                                    testVisited[tempTest].append(testDir)
                                else:
                                    testVisited[tempTest] = [testDir]
                                testGuard = tempTest
                        else:
                            break
                    coords[obstacle] = 0
                    visited[temp] = [dir]
                guard = temp
        else:
            break

    print(obstacles)
    print(time.time() - s)


def parseInput(f):
    with open(f) as file:
        return [[x for x in line.strip()] for line in file]



if __name__ == "__main__":
    main()