def main():

    crabs = parseInput("input.txt")
    crabs.sort()
    n = crabs[len(crabs) // 2]
    print(sum([abs(x - n) for x in crabs]))
    n = sum(crabs) // len(crabs)  
    print(min(sum([sum(range(1, abs(x - n) + 1)) for x in crabs]), sum([sum(range(1, abs(x - (n + 1)) + 1)) for x in crabs])))


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]

if __name__ == "__main__":
    main()