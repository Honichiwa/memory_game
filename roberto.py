import PySimpleGUI as sg
import random
import time

# bendras kortu kiekis
matches = []
for match in range(0, 4):
    matches.append(match)

# ismaisomos kortos sarase
random.shuffle(matches)

# atverstu kortu kiekis, neiskaitant suporuotu kortu
count = 0
# pirma korta (reikia logika funkcijai kad palygintu su antra korta)
pirma_korta = ""
# suporuotu kortu kiekis, reikalingas laimeti zaidima
answer_to_win = len(matches) / 2
# suporuotu kortu kiekis, su juo tikrinama ar laimejo
answer_count = 0
#answer_list = [] # kol kas nebutinas, o galbut ir visai
# kortu irasymas i zodyna, jei kortos sutampa paimami ju raktai ir pagal juos pakeiciamas kortu (butonu) veikimas
answer_dict = {}

def logika(b_key, number):
    #button_veiksmas = ""
    global count
    global pirma_korta
    global answer_count
    global answer_dict
    #global answer_list

    # kai viena korta atversta, neskaitant suporuotu kortu
    if count == 1:
        pirma_korta = b_color
        #answer_list.append(number)
        answer_dict[b_key] = matches[number]
        #print(pirma_korta)

    # kai dvi kortos atverstos, neskaitant suporuotu kortu
    if count == 2:

        # kai kortos sutampa
        if pirma_korta == b_color:
            #print("sutampa")
            #answer_list.append(number)
            answer_dict[b_key] = matches[number]
            #button_veiksmas = "sutampa"
            answer_count += 1
            for key in answer_dict:
                window[key].update(disabled=True)
            count = 0
            #answer_list = []
            answer_dict = {}
            #return button_veiksmas

        # kai kortos nesutampa
        else:
            #button_veiksmas = "nesutampa"
            #answer_list.append(number)
            answer_dict[b_key] = matches[number]
            # programos pristabdymas, kad parodyti antra atversta korta
            window.read(timeout=800)
            for key in answer_dict:
                window[key].update(button_color = ('white'))
            count = 0
            #answer_list = []
            answer_dict = {}
            #return button_veiksmas
    

# layout - jei imanoma - supaprastinti
layout = [[sg.Button("", size=(10, 4), key="-"+str(matches[0])+"-", button_color = ('white')), sg.Button("", size=(10, 4), key="-"+str(matches[1])+"-", button_color = ('white')), sg.Button("", size=(10, 4), key="-"+str(matches[2])+"-", button_color = ('white')), sg.Button("", size=(10, 4), key="-"+str(matches[3])+"-", button_color = ('white'))]]

window = sg.Window("Tile Matching Game", layout)


# mygtuku eventai ir tt
while True:
    event, values = window.read()
    if event == "-0-":
        window["-0-"].update(button_color = ('blue'))
        b_color = 'blue'
        count = count + 1
        logika("-0-", 0)
    if event == "-1-":
        window["-1-"].update(button_color = ('blue'))
        b_color = 'blue'
        count = count + 1
        logika("-1-", 1)
    if event == "-2-":
        window["-2-"].update(button_color = ('red'))
        b_color = 'red'
        count = count + 1
        logika("-2-", 2)
    if event == "-3-":
        window["-3-"].update(button_color = ('red'))
        b_color = 'red'
        count = count + 1
        logika("-3-", 3)
    if event == sg.WINDOW_CLOSED:
        break

# patestavimui ar veikia laimejimas, sitas tures but while true viduje
# gali keistis laimejimo patikrinimo logika, todel ir kintamuju gali nereiketi
if answer_to_win == answer_count:
    print("you win")

# programos uzdarymas
window.close()


### pastebejimai-pasiulymai

# pirma paklaust destytojo del programos architekturos, ir del global kintamuju

# jei viskas aisku ir jei reikia skaidyti i atskirus failus, pirmiausia tai ir padaryti

# padaryti: jei imanoma, supaprastinti koda, kur while salyga palikt kuo maziau if, o layoute, jei imanoma su for ciklu suzaist kad butu kuo maziau hardkodinimo.
# zaidimo rezultato skaiciavimo logika, logai, rezultatu saugojimas json'e, 
# menu bar virsuje programos su langais (options -> start new game, exit) (about -> highscores)
# ir tt, pildyti jei liks laiko