import re

def main():
    
    machines = parseInput("input.txt")
    
    part1 = 0
    for machine in machines:
        found = False
        for i in range(101):
            if found:
                break
            if (machine["prize"][0] - machine["a"][0] * i) % machine["b"][0] == 0 and (machine["prize"][1] - machine["a"][1] * i) % machine["b"][1] == 0:
                    j = (machine["prize"][0] - machine["a"][0] * i) // machine["b"][0]
                    if machine["prize"] == [machine["a"][0] * i + machine["b"][0] * j, machine["a"][1] * i + machine["b"][1] * j]:
                        part1 +=  i * 3 + j
                        found = True
                        
    print(part1)

    # part2
    # no brute force for me this time
    n = 10000000000000
    part2 = 0

    for machine in machines:

        equations = []
        for i in range(2):
            equations.append([machine["a"][i], machine["b"][i], machine["prize"][i] + n])

        newEquations = [[], []]
        for i in range(3):
            newEquations[0].append(equations[0][i] * equations[1][0])
            newEquations[1].append(equations[1][i] * equations[0][0])

        j = (newEquations[0][2] - newEquations[1][2]) / (newEquations[0][1] - newEquations[1][1])
        i = (equations[0][2] - equations[0][1] * j) / equations[0][0]

        if (i).is_integer() and (j).is_integer():
            part2 +=  i * 3 + j

    print(part2)
    


def parseInput(f):

    machines = []

    tmp = ["a", "b", "prize"]
    i = 0
    machine = {}

    with open(f) as file:
        for line in file:
            line = line.strip()
            if not line:
                machines.append(machine)
                i = 0
                machine = {}
            else:
                machine[tmp[i]] = [int(x) for x in re.findall(r"X.(\d+), Y.(\d+)", line)[0]]
                i += 1

    if machine:
        machines.append(machine)

    return machines


if __name__ == "__main__":
    main()