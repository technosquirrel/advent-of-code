def main():
    
    data = parseInput("input.txt")
    
    dirs = {
        "forward" : (0, 1),
        "up" : (-1, 0),
        "down" : (1, 0),
    }

    position = [0, 0]
    for line in data:
        for i in range(2):
            position[i] += dirs[line[0]][i] * line[1]
    print(position[0] * position[1])


    position = [0, 0]
    aim = 0
    for line in data:
        match line[0]:
            case "up":
                aim -= line[1]
            case "down":
                aim += line[1]
            case "forward":
                position[1] += line[1]
                position[0] += line[1] * aim
    print(position[0] * position[1])


def parseInput(f):

    data = []

    with open(f) as file:
        for line in file:
            line = line.strip().split()
            data.append([line[0], int(line[1])])

    return data


if __name__ == "__main__":
    main()