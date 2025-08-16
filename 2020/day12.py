ORDER = ["N", "E", "S", "W"]
DIRS = {"N" : (-1, 0), "E" : (0, 1), "S" : (1, 0), "W" : (0, -1)}

def main():
    
    instructions = parseInput("input.txt")
    
    direction = "E"
    index = 1
    location = [0, 0]

    for inst in instructions:

        match inst[0]:
            case "N":
                for i in range(2):
                    location[i] += DIRS["N"][i] * inst[1]
            case "S":
                for i in range(2):
                    location[i] += DIRS["S"][i] * inst[1]
            case "E":
                for i in range(2):
                    location[i] += DIRS["E"][i] * inst[1]
            case "W":
                for i in range(2):
                    location[i] += DIRS["W"][i] * inst[1]
            case "F":
                for i in range(2):
                    location[i] += DIRS[direction][i] * inst[1]
            case "L":
                n = -inst[1] // 90
                index = (index + n) % 4
                direction = ORDER[index]
            case "R":
                n = inst[1] // 90
                index = (index + n) % 4
                direction = ORDER[index]

    print(abs(location[0]) + abs(location[1]))


    # Part 2

    shipLocation = [0, 0]
    waypointLocation = [-1, 10]

    for inst in instructions:

        match inst[0]:
            case "N":
                for i in range(2):
                    waypointLocation[i] += DIRS["N"][i] * inst[1]
            case "S":
                for i in range(2):
                    waypointLocation[i] += DIRS["S"][i] * inst[1]
            case "E":
                for i in range(2):
                    waypointLocation[i] += DIRS["E"][i] * inst[1]
            case "W":
                for i in range(2):
                    waypointLocation[i] += DIRS["W"][i] * inst[1]
            case "F":
                for i in range(2):
                    shipLocation[i] += waypointLocation[i] * inst[1]
            case "L":
                if inst[1] == 90:
                    waypointLocation[0], waypointLocation[1] = -waypointLocation[1], waypointLocation[0]
                elif inst[1] == 180:
                    for i in range(2):
                        waypointLocation[i] = -waypointLocation[i]
                elif inst[1] == 270:
                    waypointLocation[0], waypointLocation[1] = waypointLocation[1], -waypointLocation[0]
            case "R":
                if inst[1] == 90:
                    waypointLocation[0], waypointLocation[1] = waypointLocation[1], -waypointLocation[0]
                elif inst[1] == 180:
                    for i in range(2):
                        waypointLocation[i] = -waypointLocation[i]
                elif inst[1] == 270:
                    waypointLocation[0], waypointLocation[1] = -waypointLocation[1], waypointLocation[0]

    print(abs(shipLocation[0]) + abs(shipLocation[1]))


def parseInput(f):

    instructions = []

    with open(f) as file:
        for line in file:
            instructions.append([line[0], int(line.strip()[1:])])

    return instructions


if __name__ == "__main__":
    main()