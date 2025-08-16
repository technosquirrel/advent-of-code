def main():
    
    planets = parseInput("input.txt")

    orbitCount = 0
    for planet in planets:
        nextPlanet = planets[planet]
        while True:
            if nextPlanet in planets:
                orbitCount += 1
                nextPlanet = planets[nextPlanet]
            else:
                orbitCount += 1
                break
    print(orbitCount)

    graph = makeGraph(planets)
    
    transfers = 0
    visited = ["YOU"]
    currentLocations = graph["YOU"]
    newLocations = set()

    while True:
        found = False
        for location in currentLocations:
            if "SAN" in graph[location]:
                print(transfers)
                found = True
                break
            else:
                try:
                    for planet in graph[location]:
                        if planet not in visited:
                            newLocations.add(planet)
                except:
                    print("pause")
                visited.append(location)

        transfers += 1
        currentLocations = [x for x in newLocations]
        newLocations = set()

        if found:
            break


def parseInput(f):

    planets = {}

    with open(f) as file:
        for line in file:
            line = line.strip().split(")")
            planets[line[1]] = line[0]

    return planets


def makeGraph(planets):
    graph = {}

    for planet in planets:
        if planet in graph:
            graph[planet].append(planets[planet])
        else:
            graph[planet] = [planets[planet]]
        if planets[planet] in graph:
            graph[planets[planet]].append(planet)
        else:
            graph[planets[planet]] = [planet]

    return graph


if __name__ == "__main__":
    main()