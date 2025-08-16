import math

class Packet:
    def __init__(self, versionId, typeId):
        self.typeId = typeId
        self.versionId = versionId
        self.contents = None
        self.literal = None


def main():
    s = hexToBin(parseInput("input.txt"))
    p = decodePacket(s)[0]
    
    print(sumPackets(p))
    print(getValue(p))


def parseInput(f):
    with open(f) as file:
        return file.readline().strip()


def decodePacket(s):
    
    if not s or all(x == "0" for x in s):
        return (None, None)
    
    subPackets = []
    packet = Packet(binToInt(s[:3]), binToInt(s[3:6]))

    if packet.typeId == 4:
        i = 6
        n = ""
        while True:
            n += s[i + 1:i + 5]
            i += 5
            if s[i - 5] == "0":
                packet.literal = binToInt(n)
                break
        return packet, s[i:]
    else:
        if s[6] == "0":
            n = binToInt(s[7:22])
            newS = s[22:22 + n]
            while True:
                p, newS = decodePacket(newS)
                if not p:
                    break
                subPackets.append(p)
            newS = s[22 + n:]
        else:
            n = binToInt(s[7:18])
            newS = s[18:]
            for i in range(n):
                p, newS = decodePacket(newS)
                if p:
                    subPackets.append(p)

        packet.contents = subPackets
        return packet, newS


def sumPackets(p):

    n = p.versionId

    if p.literal:
        return n
    else:
        for x in p.contents:
            n += sumPackets(x)

    return n


def getValue(p):

    match p.typeId:
        case 0:
            return sum(getValue(x) for x in p.contents)
        case 1:
            return math.prod(getValue(x) for x in p.contents)
        case 2:
            return min(getValue(x) for x in p.contents)
        case 3:
            return max(getValue(x) for x in p.contents)
        case 4:
            return p.literal
        case 5:
            return 1 if getValue(p.contents[0]) > getValue(p.contents[1]) else 0
        case 6:
            return 1 if getValue(p.contents[0]) < getValue(p.contents[1]) else 0
        case 7:
            return 1 if getValue(p.contents[0]) == getValue(p.contents[1]) else 0


def hexToBin(x):
    n = bin(int(x, 16))[2:]
    for c in x:
        if c == "0":
            n = "0000" + n
        else:
            break
    if len(n) % 4 != 0:
        return n.zfill(len(n) + 4 - (len(n) % 4))
    else:
        return n


def binToInt(x):
    return int(x, 2)


if __name__ == "__main__":
    main()