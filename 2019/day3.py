DIRS = {
    "U" : (0, 1),
    "D" : (0, -1),
    "L" : (-1, 0),
    "R" : (1, 0),
}

def main():
    
    instructions = parseInput("input.txt")

    wires = []

    for inst in instructions:
        wires.append(plotWire(inst))

    intersections = set([x for x in wires[0]]) & set([x for x in wires[1]])

    part1 = 999999999
    for intersection in intersections:
        x = abs(intersection[0]) + abs(intersection[1])
        if x < part1:
            part1 = x

    print(part1)

    part2 = 999999999
    for intersection in intersections:
        steps = wires[0][intersection] + wires[1][intersection]
        if steps < part2:
            part2 = steps
    print(part2)


def parseInput(f):

    with open(f) as file:
        return [line.strip().split(",") for line in file]


def plotWire(instruction):

    circuit = {}
    location = [0, 0]

    steps = 0

    for inst in instruction:
        dir = inst[0]
        x = int(inst[1:])

        for _ in range(x):
            location[0] += DIRS[dir][0]
            location[1] += DIRS[dir][1]
            steps += 1
            n = tuple(location)
            if not n in circuit:
                circuit[n] = steps

    return circuit


if __name__ == "__main__":
    main()