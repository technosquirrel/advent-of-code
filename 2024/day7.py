import time

def main():
    
    start = time.time()
    calibrations = parseInput("input.txt")
    part1 = 0
    invalid = []

    for calibration in calibrations:
        results = [calibration[0]]
        for i in range(len(calibration[1]) - 1, 0, -1):
            newResults = []
            for result in results:
                if result % calibration[1][i] == 0:
                    newResults.append(result / calibration[1][i])
                newResults.append(result - calibration[1][i])
            results = newResults
        if calibration[1][0] in results:
            part1 += calibration[0]
        else:
            invalid.append(calibration)

    print(part1)

    #part2
    part2 = 0

    for n in invalid:
        results = [n[1][0]]
        for i in range(1, len(n[1])):
            newResults = []
            for result in results:
                buffer = [result + n[1][i], result * n[1][i], int(str(result) + str(n[1][i]))]
                for res in buffer:
                    if res <= n[0]:
                        newResults.append(res)
            results = newResults
        if n[0] in results:
            part2 += n[0]

    print(part1 + part2)
    print(time.time() - start)


def parseInput(f):

    calibrations = []
    with open(f) as file:
        for line in file:
            line = line.strip().split(": ")
            calibrations.append([int(line[0]), [int(x) for x in line[1].split()]])
    return calibrations


if __name__ == "__main__":
    main()