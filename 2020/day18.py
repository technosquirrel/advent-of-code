import re

def main():
    
    expressions = parseInput("input.txt")
    
    part1 = 0
    for e in expressions:
        part1 += int(evaluate(e))
    print(part1)

    part2 = 0
    for e in expressions:
        part2 += int(evaluate2(e))
    print(part2)


def parseInput(f):
    with open(f) as file:
        return [line.strip() for line in file]


def evaluate(s):

    cpy = s
    brackets = re.findall(r"(\([^\()]+\))", cpy)

    if not brackets:
        while True:
            m = re.search(r"(\d+ [*\+] \d+)", cpy)
            if not m:
                return cpy
            else:
                cpy = cpy.replace(m[1], str(eval(m[1])), 1)
    else:
        for b in brackets:
            cpy = cpy.replace(b, evaluate(b[1:-1]), 1)
        return evaluate(cpy)


def evaluate2(s):

    cpy = s
    brackets = re.findall(r"(\([^\()]+\))", cpy)

    if not brackets:
        while True:
            m = re.search(r"(\d+ \+ \d+)", cpy)
            if not m:
                while True:
                    n = re.search(r"(\d+ \* \d+)", cpy)
                    if not n:
                        return cpy
                    else:
                        cpy = cpy.replace(n[1], str(eval(n[1])), 1)
            else:
                cpy = cpy.replace(m[1], str(eval(m[1])), 1)
    else:
        for b in brackets:
            cpy = cpy.replace(b, evaluate2(b[1:-1]), 1)
        return evaluate2(cpy)


if __name__ == "__main__":
    main()