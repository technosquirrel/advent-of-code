import re

def main():

    memory = parseInput("input.txt")
    
    matches = re.findall(r"mul\((\d{1,3},\d{1,3})\)", memory)
    part1 = 0
    
    for match in matches:
        match = [int(x) for x in match.split(",")]
        part1 += (match[0] * match[1])

    print(part1)


    state = True
    part2 = 0
    
    for i in range(len(memory)):
        s = memory[i:]
        match = re.findall(r"^mul\((\d{1,3},\d{1,3})\)", s)
        if match and state:
            m = [int(x) for x in match[0].split(",")]
            part2 += m[0] * m[1]
        if s.startswith("do()"):
            state = True
        elif s.startswith("don't()"):
            state = False
            
    print(part2)


def parseInput(f):
    s = ""
    with open(f) as file:
        for line in file:
            s += line.strip()
    return s


if __name__ == "__main__":
    main()