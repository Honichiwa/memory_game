import PySimpleGUI as sg

import tado as be
import time


layout1 = [
    [
        sg.Button(
            "Start new game",
            size=(16, 0),
            key="-new game-",
            border_width=(10),
            button_color="#ff1155",
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button(
            "Highscores", size=(16, 0), border_width=(10), button_color="#ff1155"
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button("Load game", size=(16, 0), border_width=(10), button_color="#ff1155"),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button(
            "Difficulty", size=(16, 0), border_width=(10), button_color="#ff1155"
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Output(s=(19, 20)),
    ],
    [
        sg.Button(
            "Exit",
            size=(16, 0),
            key="-EXIT-",
            border_width=(10),
            button_color="#ff1155",
        ),
        sg.Text("", size=(5, 0)),
    ],
]
layout2 = [
    [
        sg.Button(
            button_text=" ",
            size=(15, 7),
            button_color=("white"),
            key=(row, col),
            disabled=False,
        )
        for row in range(4)
    ]
    for col in range(4)
]
layout = [[sg.Col(layout1, p=0), sg.Col(layout2, p=0, visible=False, key="-COL2-")]]
# Sukuriamas langas
window = sg.Window("Tile Memory Game", layout, size=(800, 600))
# Atvaizduojame ir bendraujame su langu, naudodami įvykių kilpą
previous_event = None
score = 0
while True:
    event, values = window.read()
    # Žiūrime, ar vartotojas nori išeiti, ar langas buvo uždarytas

    # Išvedame pranešimą į langą
    if event == "-new game-":
        window["-COL2-"].update(visible=True)
    if event in be.cards:
        sg.TimerStart
        current_time = time.time()
        print(be.cards[event])
        window.read(timeout=100)
        print("pirmas if")
        window[event].update(button_color="white")
        if previous_event:
            window[previous_event].update(button_color="white")

            if be.cards[event] == be.cards[previous_event] and event != previous_event:
                score += 8
                window[previous_event].update(disabled=True)
                window[event].update(disabled=True)
                window[event].update(button_color=be.cards[event])
                window[previous_event].update(button_color=be.cards[event])
                previous_event = None
                print(score)
            else:
                window[event].update(button_color=be.cards[event])
                window.read(timeout=400)
                print("pirmas else")
                window[event].update(button_color="white")
                previous_event = None

        else:
            previous_event = event
            window[event].update(button_color=be.cards[event])
            print("antras else")

    if score == 8:
        finish_time = time.time()
        total_time = finish_time - current_time
        sg.TimerStop
        sg.popup(f"Sveikiname jus laimejote, jusu laikas: {total_time:.2f}")
        score = 0
    if event == sg.WINDOW_CLOSED or event == "-EXIT-":
        break
    # window["-Output-"].update("Game starting...")

window.close()
