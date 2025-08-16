import re

def main():
    
    data = parseInput("input.txt")

    rules = getRanges(data[0])
    myTicket = data[1]
    tickets = data[2]

    part1 = 0
    validTickets = [myTicket]

    for ticket in tickets:
        isValid = True
        for x in ticket:
            if inRange(x, rules):
                continue
            else:
                isValid = False
                part1 += x
        if isValid == True:
            validTickets.append(ticket)

    print(part1)

    rules = getRules(data[0])
    rulesFound = [[] for _ in rules]

    for i in range(len(myTicket)):
        for j in range(len(rules)):
            found = True
            for ticket in validTickets:
                if not inRange(ticket[i], rules[j]):
                    found = False
                    break
            if found == True:
                rulesFound[i].append(j)

    order = findRulesOrder(rulesFound)
    part2 = 1
    for i in range(6):
        part2 *= myTicket[order.index(i)]
    print(part2)


def parseInput(f):

    data = [[], [], []]
    i = 0

    with open(f) as file:
        for line in file:
            line = line.strip()
            if not line:
                i += 1
            elif i == 0:
                m = re.match(r".*: (\d+)-(\d+) or (\d+)-(\d+)", line)
                data[0].append([int(x) for x in m.groups()])
            elif i == 1:
                try:
                    data[1] = [int(x) for x in line.split(",")]
                except:
                    pass
            elif i == 2:
                try:
                    data[2].append([int(x) for x in line.split(",")])
                except:
                    pass
    
    return data


def getRanges(data):

    ranges = []

    for n in data:
        for i in range(0, 4, 2):
            ranges.append((n[i], n[i + 1]))
    
    ranges.sort()
    buffer = [ranges[0]]

    for i in range(1, len(ranges)):
        if ranges[i][0] > buffer[-1][1] + 1:
            buffer.append(ranges[i])
        elif ranges[i][1] <= buffer[-1][1]:
            continue
        else:
            buffer[-1] = (buffer[-1][0], ranges[i][1])

    return buffer


def inRange(x, rules):

    for r in rules:
        if r[0] <= x <= r[1]:
            return True
        
    return False


def getRules(data):

    rules = []
    for n in data:
        rules.append([(n[0], n[1]), (n[2], n[3])])
    return rules


def findRulesOrder(rules):
    
    buffer = [-1 for _ in rules]

    l = len(rules)
    for _ in range(l):
        for i, rule in enumerate(rules):
            if len(rule) == 1:
                buffer[i] = rule[0]
                n = rule[0]
                for r in rules:
                    try:
                        r.remove(n)
                    except:
                        pass
                break
            
    return buffer


if __name__ == "__main__":
    main()