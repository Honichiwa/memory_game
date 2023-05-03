import PySimpleGUI as sg
import random

def create_layout():
    matches = random.sample(range(100), 8)
    random.shuffle(matches)

    layout = []
    for row in range(2):
        row_elements = []
        for col in range(4):
            index = row * 4 + col
            button = sg.Button(
                "", size=(10, 4), key=f"-{index}-", button_color=('white', 'red', "green", "blue")
            )
            row_elements.append(button)
        layout.append(row_elements)

    return layout, matches

def run_game():
    layout, matches = create_layout()
    window = sg.Window("Tile Matching Game", layout)

    matched_indices = []
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        button_key = event
        button_value = matches[int(button_key[1:-1])]

        if button_key in matched_indices:
            continue

        window[event].update(button_color=('blue', 'white'))
        matched_indices.append(button_key)

        if len(matched_indices) == 2:
            button1, button2 = matched_indices
            if matches[int(button1[1:-1])] == matches[int(button2[1:-1])]:
                window[button1].update(disabled=True)
                window[button2].update(disabled=True)
                matched_indices = []

        if len(matched_indices) == 2:
            sg.PopupQuickMessage("No match, try again!")
            window[button1].update(button_color=('white', 'red'))
            window[button2].update(button_color=('white', 'red'))
            matched_indices = []

        if all(window[key].get_size() == (0, 0) for key in window.ElementMap()):
            sg.popup("You won!")
            break

    window.close()

if __name__ == "__main__":
    run_game()