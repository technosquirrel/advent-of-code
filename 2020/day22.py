def main():
    
    data = parseInput("input.txt")
    decks = [[x for x in deck] for deck in data]
    
    winner = 0
    while True:
        if len(decks[0]) == 0:
            winner = decks[1]
            break
        elif len(decks[1]) == 0:
            winner = decks[0]
            break
        matchUp = [decks[0].pop(0), decks[1].pop(0)]
        if matchUp[0] > matchUp[1]:
            decks[0] += matchUp
        else:
            matchUp.sort(reverse=True)
            decks[1] += matchUp
    
    print(sum(list(map(lambda x, y: x * y, winner, range(len(winner), 0, -1)))))


    # Part 2

    decks = [[x for x in deck] for deck in data]
    winner, deck = recursiveCombat(decks[0], decks[1])
    print(sum(list(map(lambda x, y: x * y, deck, range(len(deck), 0, -1)))))


def parseInput(f):

    decks = []

    with open(f) as file:
        for line in file:
            line = line.strip()
            if line.startswith("Player"):
                deck = []
            elif not line:
                decks.append(deck)
            else:
                deck.append(int(line))
    if deck not in decks:
        decks.append(deck)

    return decks


def recursiveCombat(p1, p2):
    
    decks = [[x for x in p1], [x for x in p2]]
    state = {}
    while True:
        n = (tuple(decks[0]), tuple(decks[1]))
        if n in state:
            return 0, decks[0]
        state[n] = None
        if len(decks[0]) == 0:
            return 1, decks[1]
        elif len(decks[1]) == 0:
            return 0, decks[0]
        else:
            cards = [decks[0].pop(0), decks[1].pop(0)]
            if cards[0] <= len(decks[0]) and cards[1] <= len(decks[1]):
                winner = recursiveCombat(decks[0][:cards[0]], decks[1][:cards[1]])[0]
            elif cards[0] > cards[1]:
                winner = 0
            elif cards[1] > cards[0]:
                winner = 1
            decks[winner] += [cards[winner], cards[1 - winner]]

if __name__ == "__main__":
    main()