def main():
    
    entries = parseInput("input.txt")
    for x in entries:
        if 2020 - x in entries:
            print(x * (2020 - x))
            break

    for i in range(len(entries)):
        x = entries[i]
        for j in range(i + 1, len(entries)):
            y = entries[j]
            if 2020 - x - y in entries:
                print(x * y * (2020 - x - y))
                break

def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file]


if __name__ == "__main__":
    main()