import re

def main():

    data = parseInput("input.txt")
    xLimits = data[0:2]
    xLimits.sort()
    yLimits = data[2:]
    yLimits.sort()

    y = 0
    maxY = 0

    while True:
        testY = y
        location = 0
        while True:
            location += testY
            testY -= 1
            if yLimits[0] <= location <= yLimits[1]:
                maxY = y
                break
            elif location < yLimits[0]:
                break
        if y > 100:
            print(sum([x + 1 for x in range(maxY)]))
            break
        y += 1

    # Part 2 - be better
    part2 = []
    for y in range(yLimits[0], maxY + 1):
        for x in range(xLimits[1] + 1):
            location = [0, 0]
            testX = x
            testY = y
            while True:
                location = [location[0] + testX, location[1] + testY]
                testX = max(testX - 1, 0)
                testY -= 1
                if xLimits[0] <= location[0] <= xLimits[1] and yLimits[0] <= location[1] <= yLimits[1]:
                    part2.append((x, y))
                    break
                elif location[1] < yLimits[0]:
                    break
    print(len(part2))


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in re.findall(r"(-?\d+)", file.readline())]


if __name__ == "__main__":
    main()