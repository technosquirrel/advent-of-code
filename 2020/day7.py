import re

def main():
    
    bags = parseInput("input.txt")
    target = "shiny gold"

    part1 = 0
    cache = {}
    for bag in bags:
        if containsTarget(bags, bag, target, cache):
            part1 += 1
    print(part1)

    cache = {}
    print(countContents(bags, target, cache))


def parseInput(f):

    bags = {}
    
    with open(f) as file:
        for line in file:
            line = line.strip().split(" bags contain ")
            if line[1] == "no other bags.":
                bags[line[0]] = 0
            else:
                bags[line[0]] = {}
                contents = line[1].split(", ")
                for n in contents:
                    m = re.search(r"(\d+) (\w+ \w+)", n)
                    bags[line[0]][m[2]] = int(m[1])

    return bags
    

def containsTarget(bags, current, target, cache):

    if current in cache:
        return True
    
    if bags[current] == 0:
        return False
    elif target in bags[current]:
        cache[current] = True
        return True
    else:
        newBags = bags[current]
        for bag in newBags:
            if containsTarget(bags, bag, target, cache):
                return True
        return False


def countContents(bags, bag, cache):

    if bag in cache:
        return cache[bag]
    elif not bags[bag]:
        cache[bag] = 0
        return 0
    else:
        n = 0
        for b in bags[bag]:
            n += bags[bag][b] + bags[bag][b] * countContents(bags, b, cache)
        cache[bag] = n
        return n


if __name__ == "__main__":
    main()