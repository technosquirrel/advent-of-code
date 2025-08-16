def main():
    
    data = parseInput("input.txt")
    
    current = data[0]
    part1 = 0

    for x in data:
        if x > current:
            part1 += 1
        current = x

    print(part1)


    current = sum(data[:3])
    part2 = 0

    for i in range(len(data) - 2):
        x = sum(data[i:i + 3])
        if x > current:
            part2 += 1
        current = x

    print(part2)


def parseInput(f):
    with open(f) as file:
        return [int(line.strip()) for line in file]
    

if __name__ == "__main__":
    main()