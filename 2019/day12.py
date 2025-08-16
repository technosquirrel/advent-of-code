import numpy as np

def main():
    
    moons = [[-6, 2, -9, 0, 0, 0], [12, -14, -4, 0, 0, 0], [9, 5, -6, 0, 0, 0], [-1, -4, 9, 0, 0, 0]]
    testMoons = [[-8, -10, 0, 0, 0, 0], [5, 5, 10, 0, 0, 0], [2, -7, 3, 0, 0, 0], [9, -8, -3, 0, 0, 0]]

    copy = [[x for x in moon] for moon in moons]
    simulateMotion(copy, 1000)
    print(getEnergy(copy))

    #part2
    copy = [[x for x in moon] for moon in moons]
    repeats = [False, False, False]
    i = 0

    while not all(repeats):
        for moon in copy:
            calculateVelocity(moon, copy)
        for moon in copy:
            moveMoon(moon)
        i += 1
        for j in range(3):
            if not repeats[j]:
                if isCycle(copy, j, moons):
                    repeats[j] = i

    print(np.lcm.reduce(np.array(repeats)))



def simulateMotion(moons, steps):

    for _ in range(steps):
        for moon in moons:
            calculateVelocity(moon, moons)
        for moon in moons:
            moveMoon(moon)


def calculateVelocity(moon, moons):

    for i in range(4):
        for j in range(3):
            if moon[j] > moons[i][j]:
                moon[j + 3] -= 1
            elif moon[j] < moons[i][j]:
                moon[j + 3] += 1


def moveMoon(moon):

    for j in range(3):
        moon[j] += moon[j + 3]


def getEnergy(moons):

    total = 0

    for moon in moons:
        total += (sum([abs(x) for x in moon[:3]]) * sum([abs(x) for x in moon[3:]]))

    return total


def isCycle(moons, i, start):

    velocity = [moon[i + 3] for moon in moons]
    if any(velocity):
        return False
    else:
        current = ",".join([str(moon[i]) for moon in moons])
        init = ",".join([str(moon[i]) for moon in start])
        if current == init:
            return True
        else:
            return False


if __name__ == "__main__":
    main()