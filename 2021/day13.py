import re

def main():

    points, insts = parseInput("input.txt")
    indices = {"x" : 0, "y" : 1}
    
    for i in insts:
        newPoints = set()
        for p in points:
            if p[indices[i[0]]] < i[1]:
                newPoints.add(p)
            elif p[indices[i[0]]] > i[1]:
                if i[0] == "x":
                    newPoints.add((i[1] - (p[0] - i[1]), p[1]))
                else:
                    newPoints.add((p[0], i[1] - (p[1] - i[1])))
        print(len(newPoints))
        points = newPoints

    grid = [[" " for _ in range(max(x[0] for x in points) + 1)] for _ in range(max(x[1] for x in points) + 1)]
    
    for p in points:
        grid[p[1]][p[0]] = "#"

    for line in grid:
        print("".join(line))


def parseInput(f):

    data = [[], []]

    with open(f) as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    data[0].append(tuple(int(x) for x in line.split(",")))
                except:
                    n = re.findall(r"(x|y)=(\d+)", line)[0]
                    data[1].append([n[0], int(n[1])])

    return data[0], data[1]


if __name__ == "__main__":
    main()