def main():
    
    wires, gates = parseInput("input.txt")
    part1 = runCircuit({x : wires[x] for x in wires}, gates)
    print(part1)

    # part 2
    gatesCpy = {x : gates[x] for x in gates}
    gatesReversed = {gates[x] : x for x in gates}

    carry = None
    swaps = []

    for i in range(45):

        n = str(i).zfill(2)
        x = "x" + n
        y = "y" + n
        z = "z" + n
        
        a = gates[x + " XOR " + y]
        b = gates[x + " AND " + y]
        
        if not carry:
            if a != z:
                swap(a, z, swaps, gatesCpy, gatesReversed)
            carry = b
        else:
            while True:
                buffer = [a, carry]
                buffer.sort()
                try:
                    c = gates[buffer[0] + " XOR " + buffer[1]]
                    if c != z:
                        swap(c, z, swaps, gatesCpy, gatesReversed)
                        if b == z:
                            b = c
                        c = z
                    break
                except:
                    corrected = gatesReversed[z].split()
                    wrongA = [x for x in buffer if x not in corrected and x not in [" XOR ", " OR ", " AND "]][0]
                    wrongB = [x for x in corrected if x not in buffer and x not in ["XOR", "OR", "AND"]][0]
                    swap(wrongA, wrongB, swaps, gatesCpy, gatesReversed)
                    a, b = wrongB, wrongA


            d = gatesCpy[buffer[0] + " AND " + buffer[1]]
            buffer = [b, d]
            buffer.sort()
            carry = gatesCpy[buffer[0] + " OR " + buffer[1]]

    swaps.sort()
    print(",".join(swaps))

    print(getValue(wires, "x") + getValue(wires, "y"))
    print(runCircuit({x : wires[x] for x in wires}, gatesCpy))


def parseInput(f):

    wires = {}
    gates = {}

    with open(f) as file:
        for line in file:
            line = line.strip().split(": ")
            try:
                wires[line[0]] = int(line[1])
            except:
                if line[0]:
                    line = line[0].split(" -> ")
                    tmp = line[0].split()
                    n = [tmp[0], tmp[2]]
                    n.sort()
                    tmp = [n[0], tmp[1], n[1]]
                    gates[" ".join(tmp)] = line[1]
    
    return wires, gates


def runCircuit(wires, gates):

    gatesCpy = {x : gates[x] for x in gates} 

    while True:
        newGates = {}
        for gate in gatesCpy:
            n = gate.split()
            if n[0] in wires and n[2] in wires:
                match n[1]:
                    case "AND":
                        wires[gatesCpy[gate]] = wires[n[0]] & wires[n[2]]
                    case "XOR":
                        wires[gatesCpy[gate]] = wires[n[0]] ^ wires[n[2]]
                    case "OR":
                        wires[gatesCpy[gate]] = wires[n[0]] | wires[n[2]]
                    case _:
                        raise ValueError
            else:
                newGates[gate] = gatesCpy[gate]
        if not newGates:
            return getValue(wires, "z")
        else:
            gatesCpy = newGates
        
            
def getValue(wires, c):
    n = [x for x in wires if x.startswith(c)]
    n.sort(reverse=True)
    return int("".join([str(wires[x]) for x in n]), 2)


def swap(a, b, swaps, gates, gatesRev):

    gates[gatesRev[a]], gates[gatesRev[b]] = b, a
    gatesRev[a], gatesRev[b] = gatesRev[b], gatesRev[a]
    swaps += [a, b]


if __name__ == "__main__":
    main()