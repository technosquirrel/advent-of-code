def main():

    data = parseInput("input.txt")
    fish = {i : data.count(i) for i in range(9)}
    
    for _ in range(80):
        buffer = {}
        for i in fish:
            if i == 0:
                for j in range(6, 9, 2):
                    try:
                        buffer[j] += fish[i]
                    except:
                        buffer[j] = fish[i]
            else:
                try:
                    buffer[i - 1] += fish[i]
                except:
                    buffer[i - 1] = fish[i]
        fish = buffer
    
    part1 = 0
    for i in fish:
        part1 += fish[i]
    print(part1)

    fish = {i : data.count(i) for i in range(9)}
    for _ in range(256):
        buffer = {}
        for i in fish:
            if i == 0:
                for j in range(6, 9, 2):
                    try:
                        buffer[j] += fish[i]
                    except:
                        buffer[j] = fish[i]
            else:
                try:
                    buffer[i - 1] += fish[i]
                except:
                    buffer[i - 1] = fish[i]
        fish = buffer
    
    part2 = 0
    for i in fish:
        part2 += fish[i]
    print(part2)


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip().split(",")]
    

if __name__ == "__main__":
    main()