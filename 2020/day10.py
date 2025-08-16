import functools

def main():
    
    data = parseInput("input.txt")

    adapters = [x for x in data]
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)

    part1 = [0, 0]
    for i in range(len(adapters) - 1):
        n = adapters[i + 1] - adapters[i]
        if n == 1:
            part1[0] += 1
        elif n == 3:
            part1[1] += 1
    print(part1[0] * part1[1])

    # Part 2
    end = adapters[-1]
    adapters = tuple(adapters[1:])
    print(countArrangements(0, end, adapters))


def parseInput(f):
    with open(f) as file:
        return [int(x.strip()) for x in file]


@functools.cache
def countArrangements(current, end, adapters):
    
    count = 0

    if adapters[0] == end:
        return 1
    else:
        for i in range(min(3, len(adapters))):
            if adapters[i] <= current + 3:
                count += countArrangements(adapters[i], end, adapters[i + 1:])
            else:
                return count
    return count


if __name__ == "__main__":
    main()