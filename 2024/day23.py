def  main():

    connections = parseInput("input.txt")

    part1 = set()
    for computer in connections:
        for con in connections[computer]:
            for comp in connections:
                if computer in connections[comp] and con in connections[comp]:
                    trio = [computer, con, comp]
                    trio.sort()
                    part1.add("," + ",".join(trio))
    
    count = 0
    for trio in part1:
        if ",t" in trio:
            count += 1
    print(count)

    #part2
    computers = list(connections.keys())
    computers.sort()
    
    for i, comp in enumerate(computers):
        connections[comp].sort()
        connections[comp].append(i)

    part2 = []
    for i, comp in enumerate(computers):
        parties = [[comp]]
        while True:
            newParties = []
            for party in parties:
                ind = connections[party[-1]][-1] + 1
                for j in range(ind, len(computers)):
                    if all(True if x in connections[computers[j]] else False for x in party):
                        newParties.append(party + [computers[j]])
            if len(newParties) == 0:
                part2 += parties
                break
            else:
                parties = newParties
    part2.sort(key=lambda x:len(x))
    print(",".join(part2[-1]))

def parseInput(f):

    connections = {}

    with open(f) as file:
        for line in file:
            l = line.strip().split("-")
            try:
                connections[l[0]].append(l[1])
            except:
                connections[l[0]] = [l[1]]
            try:
                connections[l[1]].append(l[0])
            except:
                connections[l[1]] = [l[0]]

    return connections


if __name__ == "__main__":
    main()