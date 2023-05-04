import random
import time

cards = {
    (0, 0): 1,
    (0, 1): 1,
    (0, 2): 2,
    (0, 3): 2,
    (1, 0): 3,
    (1, 1): 3,
    (1, 2): 4,
    (1, 3): 4,
    (2, 0): 5,
    (2, 1): 5,
    (2, 2): 6,
    (2, 3): 6,
    (3, 0): 7,
    (3, 1): 7,
    (3, 2): 8,
    (3, 3): 8,
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


# def hold(first_e, sencond_e):
#     if first_e in cards:
#         first_


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
