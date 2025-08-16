def main():
    
    caves = parseInput("input.txt")
    print(len(findAllPaths(caves, "start", "end")))
    print(len(findAllPathsRepeats(caves, "start", "end")))


def parseInput(f):

    connections = {}

    with open(f) as file:
        for line in file:
            line = line.strip().split("-")
            for i in range(2):
                try:
                    connections[line[i]].append(line[1 - i])
                except:
                    connections[line[i]] = [line[1 - i]]
    
    return connections


def findAllPaths(caves, start, end):

    paths = {}

    opts = [tuple([start])]
    while len(opts) != 0:
        p = opts.pop(0)
        if p in paths:
            continue
        elif p[-1] == end:
            paths[p] = None
        else:
            for opt in caves[p[-1]]:
                if opt in p and opt.islower():
                    continue
                newPath = tuple([x for x in p] + [opt])
                if newPath not in paths:
                    opts.append(newPath)

    return paths


def findAllPathsRepeats(caves, start, end):

    paths = {}
    opts = [[tuple([start]), ""]]

    while len(opts) != 0:
        p = opts.pop(0)
        if p[0] in paths:
            continue
        elif p[0][-1] == end:
            paths[p[0]] = None
        else:
            for opt in caves[p[0][-1]]:
                s = p[1]
                if opt == start:
                    continue
                elif opt in p[0] and opt.islower():
                    if p[1]:
                        continue
                    else:
                        s = opt
                newPath = tuple([x for x in p[0]] + [opt])
                if newPath not in paths:
                    opts.append([newPath, s])

    return paths


if __name__ == "__main__":
    main()