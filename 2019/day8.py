import numpy as np

def main():

    img = parseInput("input.txt")
    w = 25
    h = 6

    layers = []

    for i in range(0, len(img), w * h):
        layers.append(img[i : i + w * h])

    minZeroes = w * h
    part1 = 0
    for layer in layers:
        if layer.count(0) < minZeroes:
            minZeroes = layer.count(0)
            part1 = layer.count(1) * layer.count(2)

    print(part1)

    decoded = []

    for i in range(len(layers[0])):
        j = 0
        while True:
            if layers[j][i] < 2:
                decoded.append(layers[j][i])
                break
            else:
                j += 1

    decoded = np.array(decoded).reshape(h, w)

    for line in decoded:
        print("".join(["#" if x==1 else " " for x in line]))


def parseInput(f):
    with open(f) as file:
        return[int(x) for x in file.readline().strip()]



if __name__ == "__main__":
    main()