class Node:
    def __init__(self, id):
        self.id = id
        self.next = None

    def insert(self, node):
        n = self.next
        self.next = node
        node.next = n

    def delete(self):
        n = self.next
        self.next = self.next.next
        n.next = None
        return n


def main():
    n = 586439172
    test = 389125467

    cups = [int(x) for x in str(n)]
    print(orderCups(moveCups([x for x in cups], 100)))

    # Part 2

    cups = {}
    first = None
    previous = None
    for cup in [int(x) for x in str(n)] + [x for x in range(10, 1000001)]:
        c = Node(cup)
        cups[cup] = c
        if not first:
            first = c
            previous = c
        else:
            previous.next = c
            previous = c
    previous.next = first

    cup = first
    l = len(cups)
    for _ in range(10000000):
        toMove = []
        for _ in range(3):
            toMove.append(cup.delete().id)
        destination = cup.id
        while True:
            destination -= 1
            if destination == 0:
                destination = l
            if destination not in toMove:
                break
        destCup = cups[destination]
        for c in toMove:
            destCup.insert(cups[c])
            destCup = cups[c]
        cup = cup.next
    print(cups[1].next.id * cups[1].next.next.id)
        

def moveCups(cups, moves):

    l = len(cups)
    i = 0

    for x in range(moves):
        cup = cups[i]
        toMove = []
        for j in range(3):
            toMove.append(cups[(i + j + 1) % l])
        destination = cup
        for m in toMove:
            cups.remove(m)
        while True:
            destination -= 1
            if destination == 0:
                destination = l
            if destination not in toMove:
                break
        index = cups.index(destination)
        for j in range(3):
            cups.insert(index + j + 1, toMove[j])
        i = (cups.index(cup) + 1) % l

    return cups


def orderCups(cups):

    s = ""
    index = cups.index(1)
    for i in range(1, len(cups)):
        s += str(cups[(index + i) % len(cups)])
    return s


if __name__ == "__main__":
    main()