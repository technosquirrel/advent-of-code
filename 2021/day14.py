def main():
    
    s, data = parseInput("input.txt")
    
    rules = {}
    for rule in data:
        rules[rule[0]] = [rule[0][0] + rule[1], rule[1] + rule[0][1]]
    
    polymer = {}
    for i in range(len(s) - 1):
        try:
            polymer[s[i:i + 2]] += 1
        except:
            polymer[s[i:i + 2]] = 1

    for _ in range(40):
        newPolymer = {}
        for pair in polymer:
            for n in rules[pair]:
                try:
                    newPolymer[n] += polymer[pair]
                except:
                    newPolymer[n] = polymer[pair]
        polymer = newPolymer

    counts = {}
    for s in polymer:
        for c in s:
            try:
                counts[c] += polymer[s]
            except:
                counts[c] = polymer[s]
    
    for c in counts:
        if counts[c] % 2 == 0:
            counts[c] = counts[c] // 2
        else:
            counts[c] = (counts[c] + 1) // 2
    
    print(max(counts[x] for x in counts) - min(counts[x] for x in counts))


def parseInput(f):

    rules = []

    with open(f) as file:
        s = file.readline().strip()
        file.readline()
        for line in file:
            rules.append(line.strip().split(" -> "))
        
    return s, rules


if __name__ == "__main__":
    main()