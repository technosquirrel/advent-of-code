class Card:
    def __init__(self, data):
        self.data = data
        self.hits = [[False for _ in line] for line in data]
        self.complete = False

    def update(self, call):
        if self.complete:
            return False
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j] == call:
                    self.hits[i][j] = True
        return self.isWinner()
                
                
    def isWinner(self):

        for i in range(len(self.data)):
            if all(self.hits[i]):
                self.complete = True
                return True
        for i in range(len(self.data)):
            if all ([x[i] for x in self.hits]):
                self.complete = True
                return True
    
        return False
    

    def scoreCard(self):

        score = 0

        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.hits[i][j] == False:
                    score += self.data[i][j]

        return score


def main():

    calls, cardData = parseInput("input.txt")
    
    cards = []
    for card in cardData:
        cards.append(Card(card))

    scored = []

    for call in calls:
        for card in cards:
            if card.update(call):
                scored.append([card, call])
        if len(scored) == len(cards):
            break

    print(scored[0][0].scoreCard() * scored[0][1])
    print(scored[-1][0].scoreCard() * scored[-1][1])


def parseInput(f):

    cards = []

    with open(f) as file:
        calls = [int(x) for x in file.readline().split(",")]
        file.readline()
        while True:
            n = file.readline()
            if not n:
                break
            card = []
            for _ in range(5):
                card.append([int(x) for x in n.split() if x])
                n = file.readline()
            cards.append(card)

    return calls, cards


if __name__ == "__main__":
    main()