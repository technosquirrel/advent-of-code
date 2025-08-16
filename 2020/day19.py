from collections import deque
import time


def main():
    
    start = time.time()

    r, messages = parseInput("input.txt")
    rules = [0 for _ in range(max([x for x in r]) + 1)]
    for rule in r:
        rules[rule] = r[rule]

    part1 = 0
    for m in messages:
        if isValid(deque([(m, rules[0][0])]), rules):
            part1 += 1
    print(part1)

    part2 = 0
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    for m in messages:
        if isValid(deque([(m, rules[0][0])]), rules):
            part2 += 1
    print(part2)
    print(time.time() - start)
    

def parseInput(f):

    rules = {}
    messages = []
    msg = False

    with open(f) as file:
        for line in file:
            line = line.strip()
            if not line:
                msg = True
            elif not msg:
                line = line.split(": ")
                line[1] = line[1].split(" | ")
                rules[int(line[0])] = [[int(x) if x.isnumeric() else x[1:-1] for x in s.split()] for s in line[1]]
            else:
                messages.append(line)

    return rules, messages
    

def isValid(q, rules):
    
    if len(q) == 0:
        return False
    
    n = q.pop()
    s = n[0]
    pattern = n[1]

    if not s and not pattern:
        return True
    elif not s or not pattern:
        return isValid(q, rules)
    elif len(pattern) > len(s):
        return isValid(q, rules)
    else:
        try:
            buffer = rules[pattern[0]]
            for x in buffer:
                q.append((s, x + pattern[1:]))
            return isValid(q, rules)
        except:
            if s[0] == pattern[0]:
                q.append((s[1:], pattern[1:]))
            return isValid(q, rules)
    

if __name__ == "__main__":
    main()