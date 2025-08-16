import re

def main():
    
    data = parseInput("input.txt")
    
    allergens = {}
    ingredients = set()

    for k, line in enumerate(data):
        matches = re.findall(r"\(contains (.*)\)", line)
        for m in matches:
            m = m.split(", ")
            for allergen in m:
                allergens[allergen] = []
        l = line.split(" (")[0].split()
        for i in l:
            ingredients.add(i)
        data[k] = [m, l]

    for a in allergens:
        allergens[a] = list(ingredients)


    for line in data:
        for allergen in line[0]:
            buffer = []
            for ingredient in allergens[allergen]:
                if ingredient in line[1]:
                    buffer.append(ingredient)
            allergens[allergen] = buffer

    danger = set()
    for allergen in allergens:
        for i in allergens[allergen]:
            danger.add(i)

    safe = [x for x in ingredients if x not in danger]
    
    part1 = 0
    for line in data:
        for i in line[1]:
            if i in safe:
                part1 += 1
    print(part1)

    # Part 2

    part2 = {}
    while True:
        for a in allergens:
            if len(allergens[a]) == 1:
                part2[a] = allergens[a][0]
                for b in allergens:
                    if part2[a] in allergens[b]:
                        allergens[b].remove(part2[a])
        if all(True if len(allergens[x]) == 0 else False for x in allergens):
            break
    
    tmp = [x for x in part2]
    tmp.sort()
    
    for i, s in enumerate(tmp):
        tmp[i] = part2[s]
    print(",".join(tmp))


def parseInput(f):
    with open(f) as file:
        return [line.strip() for line in file]
    

if __name__ == "__main__":
    main()