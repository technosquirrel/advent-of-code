import math

def main():
    
    data = parseInput("input.txt")
    
    seaFloor = {}
    buffer = []

    for pair in data:
        if pair[0][0] == pair[1][0]:
            for i in range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1]) + 1):
                try:
                    seaFloor[(pair[0][0], i)] += 1
                except:
                    seaFloor[(pair[0][0], i)] = 1
        elif pair[0][1] == pair[1][1]:
            for i in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0]) + 1):
                try:
                    seaFloor[(i, pair[0][1])] += 1
                except:
                    seaFloor[(i, pair[0][1])] = 1
        else:
            buffer.append(pair)

    part1 = 0
    for coord in seaFloor:
        if seaFloor[coord] > 1:
            part1 += 1
    print(part1)


    for pair in buffer:
        m = 1 if pair[0][0] < pair[1][0] else -1
        n = 1 if pair[0][1] < pair[1][1] else -1
        for i, j in zip(range(pair[0][0], pair[1][0] + m, m), range(pair[0][1], pair[1][1] + n, n)):
            try:
                seaFloor[(i, j)] += 1
            except:
                seaFloor[(i, j)] = 1
    
    part2 = 0
    for coord in seaFloor:
        if seaFloor[coord] > 1:
            part2 += 1
    print(part2)



def parseInput(f):

    data = []

    with open(f) as file:
        for line in file:
            l = line.strip().split(" -> ")
            coords = []
            for i in range(2):
                coords.append(tuple(int(x) for x in l[i].split(",")))
            data.append(coords)

    return data


if __name__ == "__main__":
    main()