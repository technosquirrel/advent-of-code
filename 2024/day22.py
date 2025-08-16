import math

def main():

    secrets = parseInput("input.txt")

    part1 = []
    for secret in secrets:
        x = secret
        buffer = [x]
        for _ in range(2000):
            x = calcNewSecret(x)
            buffer.append(x)
        part1.append(buffer)

    print(sum([x[-1] for x in part1]))

    changes = []
    for seq in part1:
        buffer = []
        for i in range(len(seq) - 1):
            buffer.append(lastDigit(seq[i + 1]) - lastDigit(seq[i]))
        changes.append(buffer)

    checked = {}
    monkeys = []
    for j, change in enumerate(changes):
        monkey = {}
        for i in range(len(change) - 3):
            seq = tuple(change[i:i + 4])
            if seq not in checked:
                checked[seq] = None
            if seq not in monkey:
                monkey[seq] = lastDigit(part1[j][i + 4])
        monkeys.append(monkey)
    

    part2 = 0
    for seq in checked:
        bananas = 0
        for monkey in monkeys:
            try:
                bananas += monkey[seq]
            except:
                pass

        if bananas > part2:
            part2 = bananas

    print(part2)


def parseInput(f):
    with open(f) as file:
        return [int(x.strip()) for x in file.readlines()]

def calcNewSecret(n):

    x = n
    ops = [64, 1/32, 2048]
    for op in ops:
        x = (math.floor(x * op) ^ x) % 16777216
    return x


def lastDigit(n):
    return n - (n // 10) * 10


if __name__ == "__main__":
    main()