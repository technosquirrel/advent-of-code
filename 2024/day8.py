from itertools import combinations


def main():
    
    antennas, w, h = parseInput("input.txt")
    antinodes = {}

    for antenna in antennas:
        opts = list(combinations(antennas[antenna], 2))
        for opt in opts:
            dif = (opt[1][0] - opt[0][0], opt[1][1] - opt[0][1])
            buffer = [(opt[1][0] + dif[0], opt[1][1] + dif[1]), (opt[0][0] - dif[0], opt[0][1] - dif[1])]
            for n in buffer:
                if 0 <= n[0] < h and 0 <= n[1] < w:
                        antinodes[n] = True

    print(len(antinodes))


    #part2
    part2 = {}
    for antenna in antennas:
        opts = list(combinations(antennas[antenna], 2))
        for opt in opts:
            dif = (opt[1][0] - opt[0][0], opt[1][1] - opt[0][1])
            location = opt[0]
            while 0 <= location[0] < h and 0 <= location[1] < w:
                part2[location] = True
                location = (location[0] + dif[0], location[1] + dif[1])
            location = opt[1]
            while 0 <= location[0] < h and 0 <= location[1] < w:
                part2[location] = True
                location = (location[0] - dif[0], location[1] - dif[1])
    print(len(part2))


def parseInput(f):

    antennas = {}
    w = 0
    h = 0

    with open(f) as file:
        for i, line in enumerate(file):
            h += 1
            for j, c in enumerate(line.strip()):
                w = len(line.strip())
                coord = (i, j)
                if c != ".":
                    if c in antennas:
                        antennas[c].append(coord)
                    else:
                        antennas[c] = [coord]

    return antennas, w, h


if __name__ == "__main__":
    main()