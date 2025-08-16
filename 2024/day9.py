import time

def main():

    start = time.time()
    diskMap = parseInput("input.txt")

    filesystem = []
    id = 0
    for i, n in enumerate(diskMap):
        if i % 2 == 0:
            x = id
            id += 1
        else:
            x = -1
        filesystem.append([x, n])

    # part1
    files = [[x for x in file] for file in filesystem]

    spaceIndex = 1
    finished = False
    while not finished:
        file = files.pop()
        if file[0] > -1:
            while True:
                try:
                    if files[spaceIndex][1] == 0:
                        del files[spaceIndex]
                        spaceIndex += 1
                    elif files[spaceIndex][1] > file[1]:
                        files[spaceIndex][1] -= file[1]
                        files.insert(spaceIndex, file)
                        spaceIndex += 1
                        break
                    elif files[spaceIndex][1] == file[1]:
                        files[spaceIndex] = file
                        spaceIndex += 2
                        break
                    else:
                        x = files[spaceIndex][1]
                        files[spaceIndex] = [file[0], x]
                        file[1] -= x
                        spaceIndex += 2
                except:
                    files.append(file)
                    finished = True
                    break

    part1 = 0
    i = 0
    for file in files:
        for j in range(file[1]):
            part1 += file[0] * (i + j)
        i += file[1]
    print(part1)

    #part2
    files = [[x for x in file] for file in filesystem if file[1] > 0]
    i = len(files) - 1
    while i >= 0:
        if files[i][0] > -1:
            found = False
            for j in range(i):
                if found:
                    break
                if files[j][0] == -1:
                    if files[j][1] < files[i][1]:
                        continue
                    elif files[j][1] == files[i][1]:
                        files[j], files[i] = files[i], files[j]
                        found = True
                        i -= 1
                    else:
                        file = [x for x in files[i]]
                        files[j][1] -= file[1]
                        files.insert(j, file)
                        files[i + 1][0] = -1
                        found = True
            if not found:
                i -= 1
        else:
            i -= 1

    part2 = 0
    i = 0
    for file in files:
        if file[0] > -1:
            for j in range(file[1]):
                part2 += file[0] * (i + j)
        i += file[1]
    print(part2)
    print(time.time() - start)


def parseInput(f):
    with open(f) as file:
        return [int(x) for x in file.readline().strip()]


if __name__ == "__main__":
    main()