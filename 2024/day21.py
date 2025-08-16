import numpy as np
import time


DIRS = {(-1, 0) : "^", (0, 1) : ">", (1, 0) : "v", (0, -1) : "<"}
DIRS_REVERSE = {"^" : (-1, 0), ">" : (0, 1), "v" : (1, 0), "<" : (0, -1)}

def main():
    
    start = time.time()
    codes = parseInput("input.txt")
    
    pads = {
        "dir" : [
            [None, "^", "A"],
            ["<", "v", ">"]
        ],
        "num" : [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, "0", "A"]
        ]
    }

    keypads = {}
    for pad in pads:
        keypads[pad] = getMappings(pads[pad])

    mappings = {}
    for pad in keypads:
        for m in keypads[pad]:
            if m not in mappings:
                mappings[m] = {}
            for n in keypads[pad][m]:
                if len(keypads[pad][m][n]) == 1:
                    keypads[pad][m][n] = keypads[pad][m][n].pop()
                else:
                    keypads[pad][m][n] = findShortest(keypads[pad][m][n], keypads["dir"])
                mappings[m][n] = keypads[pad][m][n]

    # Now the real work begins

    part1 = 0
    cache = {}
    for code in codes:
        n = {code : 1}
        for _ in range(3):
            n = expand(n, mappings, cache)
        part1 += getLength(n) * int(code[:-1])
    print(part1)

    part2 = 0
    for code in codes:
        n = {code : 1}
        for _ in range(26):
            n = expand(n, mappings, cache)
        part2 += getLength(n) * int(code[:-1])
    print(part2)
    print(time.time() - start)


def parseInput(f):
    with open(f) as file:
        return [line.strip() for line in file]


def getMappings(pad):

    mappings = {}

    for i in range(len(pad)):
        for j in range(len(pad[0])):
            if pad[i][j]:
                mappings[pad[i][j]] = {}
                for x in range(len(pad)):
                    for y in range(len(pad[0])):
                        if pad[x][y] == pad[i][j]:
                            mappings[pad[i][j]][pad[x][y]] = ["A"]
                        elif pad[x][y]:
                            seq = "" 
                            change = (x - i, y - j)
                            for k, n in enumerate(change):
                                dir = np.sign(n)
                                for d in DIRS:
                                    if d[k] == dir:
                                        seq += (DIRS[d] * abs(n))
                            mappings[pad[i][j]][pad[x][y]] = set()
                            if isValid((i, j), seq, pad):
                                mappings[pad[i][j]][pad[x][y]].add(seq + "A")
                            if isValid((i, j), seq[::-1], pad):
                                mappings[pad[i][j]][pad[x][y]].add(seq[::-1] + "A")    
    
    return mappings


def isValid(l, moves, pad):

    for move in moves:
        l = (l[0] + DIRS_REVERSE[move][0], l[1] + DIRS_REVERSE[move][1])
        if not pad[l[0]][l[1]]:
            return False
    return True


def findShortest(seqs, mappings):
    n = [x for x in seqs]
    cpy = [[x] for x in seqs]
    while True:
        buffer = []
        for seq in cpy:
            for opt in seq:
                newSeqs = [""]
                current = "A"
                for c in opt:
                    tmp = []
                    if type(mappings[current][c]) == str:
                        for y in newSeqs:
                            tmp.append(y + mappings[current][c])
                    else:
                        for x in mappings[current][c]:
                            for y in newSeqs:
                                tmp.append(y + x)
                    newSeqs = tmp
                    current = c
            newSeqs.sort(key=lambda x:len(x))
            newSeqs = [x for x in newSeqs if len(x) == len(newSeqs[0])]
            buffer.append(newSeqs)
        if len(buffer[0][0]) == len(buffer[1][0]):
            cpy = buffer
        elif len(buffer[0][0]) < len(buffer[1][0]):
            return n[0]
        elif len(buffer[0][0]) > len(buffer[1][0]):
            return n[1]
        

def expand(code, mappings, cache):
    
    buffer = {}

    for seq in code:
        try:
            n = cache[seq]
        except:
            s = ""
            current = "A"
            for c in seq:
                s += mappings[current][c]
                current = c
            splits = splitOnA(s)
            n = {}
            for x in splits:
                try:
                    n[x] += 1
                except:
                    n[x] = 1
            cache[seq] = n
        
        for x in n:
            try:
                buffer[x] += n[x] * code[seq]
            except:
                buffer[x] = n[x] * code[seq]

    return buffer


def splitOnA(s):

    buffer = []
    sub = ""
    for c in s:
        sub += c
        if c == "A":
            buffer.append(sub)
            sub = ""
    return buffer


def getLength(seq):

    x = 0
    for n in seq:
        x += len(n) * seq[n]
    return x


if __name__ == "__main__":
    main()