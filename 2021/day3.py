def main():
    
    data = parseInput("input.txt")
    
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        buffer = [x[i] for x in data]
        if buffer.count("0") > buffer.count("1"):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    print(int(gamma, 2) * int(epsilon, 2))

    oxygen = [x for x in data]
    carbon = [x for x in data]

    for i in range(len(data[0])):
        if len(oxygen) == 1:
            break
        o = [x[i] for x in oxygen]
        n = "0"
        if o.count("1") >= o.count("0"):
            n = "1"
        buffer = []
        for x in oxygen:
            if x[i] == n:
                buffer.append(x)
        oxygen = buffer

    for i in range(len(data[0])):
        if len(carbon) == 1:
            break
        c = [x[i] for x in carbon]
        n = "1"
        if c.count("0") <= c.count("1"):
            n = "0"
        buffer = []
        for x in carbon:
            if x[i] == n:
                buffer.append(x)
        carbon = buffer

    print(int("".join(oxygen[0]), 2) * int("".join(carbon[0]), 2))    


def parseInput(f):
    with open(f) as file:
        return [[x for x in line.strip()] for line in file]
    

if __name__ == "__main__":
    main()