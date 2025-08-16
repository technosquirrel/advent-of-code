import re

def main():
    
    insts = parseInput("test.txt")
    for i, line in enumerate(insts):
        insts[i] = [line[0], tuple(x + 1 if n % 2 == 1 else x for n, x in enumerate(line[1:]))]

    part1 = initialize(insts, -50, 50)
    print(part1)


def parseInput(f):

    insts = []

    with open(f) as file:
        for line in file:
            m = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
            insts.append([m.groups()[0]] + [int(x) for x in m.groups()[1:]])

    return insts


def initialize(insts, min, max):

    cubes = []
    v = 0

    for line in insts:
        for cube in cubes:
            overlaps = []
            v -= getOverlap(line[1], cube)
        if line[0] == "on":
            v += calcVolume(line[1])
            cubes.append(line[1])

    return v


def getOverlap(c1, c2):
    return max(0, (min(c1[1], c2[1]) - max(c1[0], c2[0]))) * max(0, (min(c1[3], c2[3]) - max(c1[2], c2[2]))) * max(0, (min(c1[5], c2[5]) - max(c1[4], c2[4])))


def calcVolume(c):
    return (c[1] - c[0]) * (c[3] - c[2]) * (c[5] - c[4])


if __name__ == "__main__":
    main()