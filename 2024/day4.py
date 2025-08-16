def main():

    wordsearch = parseInput("input.txt")
    w = len(wordsearch[0])
    h = len(wordsearch)

    part1 = 0
    valid = ["XMAS", "SAMX"]
    for i in range(h):
        for j in range(w):
            words = ["" for _ in range(4)]
            words[0] += "".join(wordsearch[i][j : min(j + 4, w)])
            for n in range(4):
                if i + n < h:
                    words[1] += wordsearch[i + n][j]
                    if j + n < h:
                        words[2] += wordsearch[i + n][j + n]
                    if j - n >= 0:
                        words[3] += wordsearch[i + n][j - n]
            for word in words:
                if word in valid:
                    part1 += 1
    print(part1)

    #part2

    part2 = 0
    valid = ["MAS", "SAM"]
    for i in range(h - 2):
        for j in range(w - 2):
            words = ["", ""]
            for n in range(3):
                words[0] += wordsearch[i + n][j + n]
                words[1] += wordsearch[i + 2 - n][j + n]
            if words[0] in valid and words[1] in valid:
                part2 += 1
    print(part2)


def parseInput(f):
    with open(f) as file:
        return [[x for x in line.strip()] for line in file]
    

if __name__ == "__main__":
    main()