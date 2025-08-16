def main():
    
    grid = parseInput("input.txt")

    part1 = countTrees(grid, (1, 3))
    print(part1)

    part2 = part1
    slopes = [(1, 1), (1, 5), (1, 7), (2, 1)]
    for slope in slopes:
        part2 *= countTrees(grid, slope)
    print(part2)


def parseInput(f):
    with open(f) as file:
        return [[x for x in line.strip()] for line in file]
    

def countTrees(grid, slope):

    i = 0
    j = 0
    trees = 0

    while i < len(grid):
        if grid[i][j] == "#":
            trees += 1
        i += slope[0]
        j = (j + slope[1]) % len(grid[0])

    return trees


if __name__ == "__main__":
    main()