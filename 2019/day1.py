def main():
    
    modules = parseInput("input.txt")

    part1 = 0
    for module in modules:
        part1 += calculateFuel(module)
    print(part1)

    part2 = 0
    for module in modules:
        x = module
        while True:
            x = calculateFuel(x)
            if x <= 0:
                break
            else:
                part2 += x
    print(part2)


def parseInput(f):

    with open(f) as file:
        return [int(x) for x in file]


def calculateFuel(x):
    return x // 3 - 2


if __name__ == "__main__":
    main()