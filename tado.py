import random

cards = {"a": 1, "b": 1, "c": 2, "d": 2, "e": 3, "f": 3, "g": 4, "h": 4}
values = list(cards.values())

random.shuffle(values)

for key, value in cards.items():
    cards[key] = values.pop(0)

print(cards)


def matching(first, second):
    if cards[first] == cards[second]:
        return True
    else:
        return False


def game(first=input("iveskite pirma raide: "), second=input("iveskite antra raide: ")):
    if matching(first, second) == True:
        # del cards[first], cards[second]
        print("super")

    if matching(first, second) == False:
        print("neteisingas spejimas")

    if cards == {}:
        print("laimejote")


game()
