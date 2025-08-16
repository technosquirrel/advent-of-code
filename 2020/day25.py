def main():
    keys = [12578151, 5051300]
    loops = [0, 0]

    i = 0
    x = 1
    while True:
        x = (x * 7) % 20201227
        for j in range(2):
            if x == keys[j]:
                loops[j] = i + 1
        if loops[0] != 0 and loops[1] != 0:
            break
        i += 1

    x = keys[0]
    for i in range(loops[1] - 1):
        x = (x * keys[0]) % 20201227
    print(x)
    x = keys[1]
    for i in range(loops[0] - 1):
        x = (x * keys[1]) % 20201227
    print(x)

if __name__ == "__main__":
    main()