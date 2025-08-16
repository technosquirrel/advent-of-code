import re

class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self, gridW, gridH, steps=1):
        self.x = (self.x + steps * self.dx) % gridW
        self.y = (self.y + steps * self.dy) % gridH


def main():
    
    robots = parseInput("input.txt")
    w = 101
    h = 103

    quadrants = [[0, 0], [0, 0]]

    for robot in robots:
        robot.move(w, h, 100)
        if robot.y < h // 2:
            if robot.x < w // 2:
                quadrants[0][0] += 1
            elif robot.x > w // 2:
                quadrants[0][1] += 1
        elif robot.y > h // 2:
            if robot.x < w // 2:
                quadrants[1][0] += 1
            elif robot.x > w // 2:
                quadrants[1][1] += 1

    print(quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1])

    #part2
    robots = parseInput("input.txt")
    grid = [[" " for _ in range(w)] for _ in range(h)]

    # h = 103x + 63
    # v = 101y + 82

    for robot in robots:
        robot.move(w, h, 63)
    seconds = 63

    while True:
        grid = [[" " for _ in range(w)] for _ in range(h)]
        for robot in robots:
            robot.move(w, h, 103)
            grid[robot.y][robot.x] = "▉"
        for line in grid:
            print("".join(line))
        seconds += 103
        print(seconds)
        input()



def parseInput(f):

    robots = []
    
    with open(f) as file:
        for line in file:
            nums = re.findall(r"(-?\d+)", line)
            robots.append(Robot(*[int(x) for x in nums]))
    
    return robots


if __name__ == "__main__":
    main()