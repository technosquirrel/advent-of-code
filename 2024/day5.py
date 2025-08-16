def main():

    rules, rulesInverted, manuals = parseInput("input.txt")
    
    sortedManuals = []

    part1 = 0
    for manual in manuals:
        sortedManual = customSort(manual, rules, rulesInverted)
        if manual == sortedManual:
            part1 += manual[len(manual) // 2]
        else:
            sortedManuals.append(sortedManual)
    print(part1)

    part2 = 0
    for manual in sortedManuals:
        part2 += manual[len(manual) // 2]
    print(part2)


def parseInput(f):
    
    rules = {}
    rulesInverted = {}

    manuals = []

    with open(f) as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    l = line.split("|")
                    l = [int(x) for x in l]
                    if l[0] in rules:
                        rules[l[0]].append(l[1])
                    else:
                        rules[l[0]] = [l[1]]
                    if l[1] in rulesInverted:
                        rulesInverted[l[1]].append(l[0])
                    else:
                        rulesInverted[l[1]] = [l[0]]
                except:
                    l = line.split(",")
                    manuals.append([int(x) for x in l])

        return rules, rulesInverted, manuals


def customSort(manual, rules, rulesInverted):

    customRules = shrinkRules(rules, manual)
    customInverted = shrinkRules(rulesInverted, manual)

    sortedManual = []
    while len(customRules) > 0:
        for rule in customRules:
            if rule not in customInverted:
                sortedManual.append(rule)
                for n in customRules[rule]:
                    customInverted[n].remove(rule)
                    if len(customInverted[n]) == 0:
                        del customInverted[n]
                del customRules[rule]
                break
    
    for n in manual:
        if n not in sortedManual:
            sortedManual.append(n)

    return sortedManual


def shrinkRules(rules, manual):

    buffer = {rule:[x for x in rules[rule] if x in manual] for rule in rules if rule in manual}
    smallRules = {}
    for r in buffer:
        if buffer[r] != []:
            smallRules[r] = buffer[r]

    return smallRules



if __name__ == "__main__":
    main()