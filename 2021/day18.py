import re
import math
from itertools import permutations
import time

def main():
    s = time.time()
    homework = parseInput("input.txt")

    answer = ""
    for line in homework:
        if not answer:
            answer = snailReduce(line)
        else:
            answer = snailAdd(answer, line)

    print(calculateMagnitude(answer))

    opts = permutations(homework, 2)
    part2 = 0
    for opt in opts:
        x = calculateMagnitude(snailAdd(opt[0], opt[1]))
        if x > part2:
            part2 = x
    print(part2)
    print(time.time() - s)


def parseInput(f):
    with open(f) as file:
        return [line.strip() for line in file]
    

def snailReduce(s): 
    
    cpy = s

    while True:
        tmp = snailExplode(cpy)
        if tmp:
            cpy = tmp
            continue
        tmp = snailSplit(cpy)
        if tmp:
            cpy = tmp
            continue
        return cpy



def snailAdd(s1, s2):
    return snailReduce("[" + s1 + "," + s2 + "]")


def snailExplode(s):

    layer = 0
    tmp = ""
    for i, c in enumerate(s):
        if c == ",":
            continue
        elif c == "[":
            layer += 1
        elif c == "]":
            layer -= 1
        elif layer > 4:
            nums = re.findall(r"^(\d+,\d+)", s[i:])
            if not nums:
                continue
            n = [int(x) for x in nums[0].split(",")]
            buffer = s[:i - 1][::-1]
            m = re.findall(r"(\d+)", buffer)
            if m:
                tmp = buffer.replace(m[0], str(int(m[0][::-1]) + n[0])[::-1], 1)[::-1] + "0"
            else:
                tmp = s[:i - 1] + "0"
            buffer = s[i + len(nums[0]) + 1:]
            m = re.findall(r"(\d+)", buffer)
            if m:
                tmp += buffer.replace(m[0], str(int(m[0]) + n[1]), 1)
            else:
                tmp += buffer
            return tmp
    
    return False


def snailSplit(s):
    
    m = re.findall(r"(\d+)", s)
    for x in m:
        if len(x) > 1:
            tmp = s.replace(x, "[" + str(int(x) // 2) + "," + str(math.ceil(int(x) / 2)) + "]", 1)
            return tmp
    return False


def calculateMagnitude(s):

    cpy = s
    while True:
        m = re.findall(r"(\[\d+,\d+\])", cpy)
        if not m:
            return int(cpy)
        for x in m:
            cpy = cpy.replace(x, snailSum(x), 1)


def snailSum(s):
    n = s[1:-1].split(",")
    return str(int(n[0]) * 3 + int(n[1]) * 2)


if __name__ == "__main__":
    main()