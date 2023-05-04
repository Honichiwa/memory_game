import random
import time

cards = {
    (0, 0): "green",
    (0, 1): "green",
    (0, 2): "red",
    (0, 3): "red",
    (1, 0): "yellow",
    (1, 1): "yellow",
    (1, 2): "blue",
    (1, 3): "blue",
    (2, 0): "orange",
    (2, 1): "orange",
    (2, 2): "pink",
    (2, 3): "pink",
    (3, 0): "teal",
    (3, 1): "teal",
    (3, 2): "cyan",
    (3, 3): "cyan",
}
values = list(cards.values())

random.shuffle(values)

for key, value in cards.items():
    cards[key] = values.pop(0)


def matching(first, second):
    if cards[first] == cards[second]:
        return True
    else:
        return False


def kordinate(x, y):
    return (x, y)


def game(first, second):
    while len(cards) >= 2:
        if matching(first, second):
            del cards[first], cards[second]
            print("super")

        else:
            print("neteisingas spejimas")

        if cards == {}:
            print("laimejote")
