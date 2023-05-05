import random


cards = {
    (0, 0): "small_swift.png",
    (0, 1): "small_swift.png",
    (0, 2): "small_html.png",
    (0, 3): "small_html.png",
    (1, 0): "small_ruby.png",
    (1, 1): "small_ruby.png",
    (1, 2): "small_pytho.png",
    (1, 3): "small_pytho.png",
    (2, 0): "small_javascript.png",
    (2, 1): "small_javascript.png",
    (2, 2): "small_php.png",
    (2, 3): "small_php.png",
    (3, 0): "small_csharp.png",
    (3, 1): "small_csharp.png",
    (3, 2): "small_java.png",
    (3, 3): "small_java.png",
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

def sort_highscores(sorted_highscores):
    for keys, values in sorted_highscores.items():
	    print(f"{keys} s : {values}")
