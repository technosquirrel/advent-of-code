def main():

    locations = parseInput("input.txt")

    for l in locations:
        l.sort()

    part1 = 0
    for i, v in enumerate(locations[0]):
        part1 += abs(v - locations[1][i])
    print(part1)

    part2 = 0
    for location in locations[0]:
        part2 += location * locations[1].count(location)
    print(part2)


def parseInput(f):

    locations = [[], []]

    with open(f) as file:
        for line in file:
            line = line.split()
            for i in range(2):
                locations[i].append(int(line[i]))

    return locations


if __name__ == "__main__":
    main()