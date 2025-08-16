from itertools import permutations, product, combinations

PERMUTES = list(permutations(range(3)))
SIGNS = list(product((1, -1), repeat=3))

def main():
    
    scanners = parseInput("input.txt")
    found = {0 : (0, 0, 0)}
    beacons = set()
    refs = [[tuple(x) for x in scanners[0]]]

    for x in refs[0]:
        beacons.add(x)

    while len(found) != len(scanners):
        newRefs = []
        for i in range(len(scanners)):
            for ref in refs:
                if i not in found:
                    bs, c = findBeacons(ref, scanners[i], 12)
                    if bs:
                        for b in bs:
                            beacons.add(b)
                        newRefs.append(list(bs))
                        found[i] = c
                        if len(found) == len(scanners):
                            print(len(beacons))
                            print(getManhattanDistance([found[x] for x in found]))
                            return
        refs = newRefs


def parseInput(f):

    scanners = []
    with open(f) as file:
        for line in file:
            if not line.strip():
                continue
            elif "scanner" in line:
                try:
                    scanners.append(scanner)
                except:
                    pass
                scanner = []
            else:
                scanner.append([int(x) for x in line.strip().split(",")])
    if scanner:
        scanners.append(scanner)

    return scanners


def findBeacons(ref, scanner, overlap):

    for p in PERMUTES:
        for s in SIGNS:
            for i in range(len(scanner) - overlap + 1):
                for j in range(len(ref)):
                    overlaps = set()
                    beacons = []
                    c = tuple(ref[j][x] - scanner[i][p[x]] * s[x] for x in range(3))
                    for scan in scanner:
                        b = tuple(scan[p[x]] * s[x] + c[x] for x in range(3))
                        beacons.append(b)
                        if b in ref:
                            overlaps.add(b)
                    if len(overlaps) >= overlap:
                        return beacons, c
    
    return None, None


def getManhattanDistance(coords):

    x = 0
    combs = combinations(range(len(coords)), 2)

    for c in combs:
        n = abs(coords[c[0]][0] - coords[c[1]][0]) + abs(coords[c[0]][1] - coords[c[1]][1]) + abs(coords[c[0]][2] - coords[c[1]][2])
        if n > x:
            x = n

    return x


if __name__ == "__main__":
    main()