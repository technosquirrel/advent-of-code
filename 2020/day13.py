def main():
    
    timestamp, buses = parseInput("input.txt")
    realBuses = [int(x) for x in buses if x.isnumeric()]
    
    part1 = timestamp
    b = 0
    for bus in realBuses:
        n = bus - (timestamp % bus)
        if n < part1:
            part1 = n
            b = bus
    print(part1 * b)

    # Part 2
    vals = []
    remainders = []
    for i, bus in enumerate(buses):
        try:
            b = int(bus)
            vals.append(b)
            remainders.append(b - i)
        except:
            pass

    print(CRT(vals, remainders))


def parseInput(f):
    with open(f) as file:
        timestamp = int(file.readline().strip())
        buses = file.readline().strip().split(",")
    return timestamp, buses


def CRT(nums, rems):

    res = 0
    prod = 1

    for n in nums:
        prod *= n

    for i, n in enumerate(nums):
        pp = prod // n
        res += pp *  rems[i] * pow(pp, -1, n)

    return res % prod


if __name__ == "__main__":
    main()