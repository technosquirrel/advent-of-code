from functools import cache
import time


def main():
    
    start = time.time()
    towels, designs = parseInput("input.txt")

    part1 = []
    for design in designs:
        if isValid(design, towels):
            part1.append(design)
    print(len(part1))

    part2 = []
    for design in part1:
        part2.append(countArrangements(design, towels))
    print(sum(part2))
    print(time.time() - start)


def parseInput(f):
    with open(f) as file:
        towels = tuple(file.readline().strip().split(", "))
        file.readline()
        return towels, [line.strip() for line in file]


def isValid(design, towels):

    if design in towels:
        return True
    else:
        for towel in towels:
            if design.startswith(towel):
                if isValid(design[len(towel):], towels):
                    return True
                
    return False


@cache
def countArrangements(design, towels):
    
    count = 0
    
    if design in towels:
        count += 1

    for towel in towels:
        if design.startswith(towel):
            count += countArrangements(design[len(towel):], towels)

    return count


if __name__ == "__main__":
    main()