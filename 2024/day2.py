def main():

    reports = parseInput("input.txt")

    part1 = 0
    for report in reports:
        if checkValid(report):
            part1 += 1
    print(part1)

    part2 = 0
    for report in reports:
        for i in range(len(report)):
            if checkValid([x for j, x in enumerate(report) if j != i]):
                part2 +=1
                break
    print(part2)


def parseInput(f):
    with open(f) as file:
        return [[int(x) for x in line.split()] for line in file]
    

def checkValid(report):

    copy = tuple(report)
    if tuple(sorted(report)) != copy and tuple(sorted(report, reverse=True)) != copy:
        return False
    elif len(set(report)) != len(report):
        return False
    else:
        for i in range(len(report) - 1):
            if abs(report[i] - report[i + 1]) > 3:
                return False
            
    return True
    

if __name__ == "__main__":
    main()