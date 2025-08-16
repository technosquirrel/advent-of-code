import numpy as np
import math

def main():
    
    map = parseInput("input.txt")
    asteroids = {}

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                asteroids[(i, j)] = []

    checked = {}
    for station in asteroids:
        checked[station] = True
        for asteroid in asteroids:
            if asteroid not in checked:
                if checkSight(station, asteroid, asteroids):
                    asteroids[station].append(asteroid)
                    asteroids[asteroid].append(station)

    maxAsteroids = 0
    station = (0, 0)
    for asteroid in asteroids:
        if len(asteroids[asteroid]) > maxAsteroids:
            maxAsteroids = len(asteroids[asteroid])
            station = asteroid

    print(maxAsteroids)

    #part2

    angles = {}

    start = np.array([-1, 0])
    del asteroids[station]

    for asteroid in asteroids:
        angle = float(findAngle(start, station, asteroid))
        if angle in angles:
            angles[angle].append(asteroid)
        else:
            angles[angle] = [asteroid]

    for angle in angles:
        angles[angle] = sorted(angles[angle], key=lambda x: getDistance(x, station))

    orderedAngles = sorted([x for x in angles])
    index = 0

    destroyed = []
    for i in range(200):
        while True:
            a = orderedAngles[index]
            if a in angles:
                destroyed.append(angles[a][0])
                del angles[a][0]
                if len(angles[a]) == 0:
                    del angles[a]
                index = (index + 1) % len(orderedAngles)
                break
            else:
                index = (index + 1) % len(orderedAngles)
    
    print(destroyed[-1][1] * 100 + destroyed[-1][0])


def parseInput(f):
    with open(f) as file:
        return[[1 if x == "#" else 0 for x in line.strip()] for line in file]
    

def checkSight(a1, a2, asteroids):

    vec = [a2[0] - a1[0], a2[1] - a1[1]]
    gdc = int(np.gcd(vec[0], vec[1]))
    vec = [x / gdc for x in vec]

    pos = [x for x in a1]

    while True:

        for i in range(2):
            pos[i] += vec[i]

        if pos[0] == a2[0] and pos[1] == a2[1]:
            return True
        elif (pos[0], pos[1]) in asteroids:
            return False


def findAngle(start, a1, a2):
    vec = np.array([a2[0] - a1[0], a2[1] - a1[1]])
    cosTheta = np.dot(start, vec) / (np.linalg.norm(start) * np.linalg.norm(vec))
    angle = np.arccos(np.clip(cosTheta, -1.0, 1.0))
    if a2[1] < a1[1]:
        angle = 2 * math.pi - angle
    return round(angle, 3)
    

def getDistance(a1, a2):
    return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])


if __name__ == "__main__":
    main()