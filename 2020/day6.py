def main():
    
    groups = parseInput("input.txt")
    
    part1 = 0
    for group in groups:
        g = "".join(group)
        part1 += len(set(x for x in g))
    print(part1)

    part2 = 0
    for group in groups:
        n = 0
        for c in group[0]:
            valid = True
            for i in range(len(group)):
                if c not in group[i]:
                    valid = False
                    break
            if valid:
                n += 1
        part2 += n
    print(part2)


def parseInput(f):

    groups = []

    with open(f) as file:
        group = []
        for line in file:
            line = line.strip()
            if line:
                group.append(line)
            else:
                groups.append(group)
                group = []

    if group:
        groups.append(group)

    return groups
    

if __name__ == "__main__":
    main()