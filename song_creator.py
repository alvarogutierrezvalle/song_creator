import random
import winsound
from tkinter import *
from tkinter import ttk
from playsound import playsound
import numpy as nup
from scipy.io.wavfile import write
from pydub import *
import os

# Constantes
figuras = {'b': 2, 'np': 1.5, 'n': 1, 'c': 0.5}
tempo = 600
duracion = {'b': (tempo * 2), 'np': int(tempo * 1.5), 'n': tempo, 'c': int(tempo / 2), 's': int(tempo / 4)}
notas = ('do', 're', 'mi', 'fa', 'sol', 'la', 'si')
primera_nota = {'DoM': ('do', 'mi', 'sol'), 'SolM': ('re', 'si', 'sol'), 'FaM': ('do', 'fa', 'la'),
                'Lam': ('do', 'mi', 'la')}
last_compas = ['Do', ['do'], ['b']]
sonidos = {'do': 261, 're': 293, 'mi': 329, 'fa': 349, 'sol': 392, 'la': 440, 'si': 494}

# Añadir sucesiones tipicas de acordes

secuencias = {'alegre1': ('DoM', 'SolM', 'FaM', 'SolM', 'DoM', 'SolM', 'FaM', 'SolM'),
              'alegre2': ('DoM', 'DoM', 'SolM', 'SolM', 'FaM', 'FaM', 'SolM', 'SolM'),
              'alegre3': ('DoM', 'Lam', 'FaM', 'SolM', 'DoM', 'Lam', 'FaM', 'SolM'),
              'epica': ('Lam', 'FaM', 'DoM', 'SolM', 'Lam', 'FaM', 'DoM', 'SolM')
              }

waves = {
    'Do': 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\Do.wav',
    'DoM': 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\DoM.wav',
    'SolM': 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\SolM.wav',
    'FaM': 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\FaM.wav',
    'Lam': 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\Lam.wav'
}

canciones = []


def secuencia(secu):
    return secuencias[secu]


def crear_figuras():
    new_compas = []

    # hacemos una lista de las figuras

    lista_figura = list(figuras)

    # Elección de la primera nota(varía del resto) Se evita que el compas empiece con una semicorchea

    figura1 = random.choice(lista_figura)
    new_compas.append(figura1)
    tiempo = figuras[figura1]

    while tiempo != 2:
        new_figura = random.choice(lista_figura[1:])
        if (tiempo + figuras[new_figura]) > 2:
            pass
        else:
            new_compas.append(new_figura)
            tiempo += figuras[new_figura]
    return new_compas


def crear_melodia(acorde, compas):
    melodia = []
    # PRIMERA NOTA:
    nota1 = random.choice(primera_nota[acorde])
    melodia.append(nota1)

    for n in range(1, len(compas)):
        melodia.append(random.choice(notas))
    return melodia


def componer():
    sec = opciones.get()
    compases = 0
    song = []
    secun = secuencia(sec)
    for long in range(0, 8):
        print(f'\nCompas nº{(long + 1)}')
        acorde = secun[long]
        compas = crear_figuras()
        melodia = crear_melodia(acorde, compas)
        song.append([acorde, melodia, compas])
        print([acorde, melodia, compas])
        compases += 1

    print(f'\nCompas nº{(compases + 1)}')
    song.append(last_compas)
    print(last_compas)
    canciones.append(song)
    reproducir()


def notado(nota, figur):
    n_final = sonidos[nota]
    time = duracion[figur]
    return winsound.Beep(n_final, time)


def reproducir():
    song = canciones[-1]
    for comp in range(len(song)):
        playsound(waves[song[comp][0]], False)
        for note in range(len(song[comp][1])):
            notado(song[comp][1][note], song[comp][2][note])


# ----------------GUARDAR-----------------------------------------

sps = 44100
vol = 0.3

def notado_2(nota, figur, post):
    n_final = sonidos[nota]
    time = duracion[figur]
    esm = nup.arange(time / 1000 * sps)
    wf1 = nup.sin(2 * nup.pi * esm * n_final / sps) * vol
    wf_int1 = nup.int16(wf1 * 32767)
    write(f"sample{post}.wav", sps, wf_int1)


def guardar():
    complete = AudioSegment.empty()
    post = 0
    cancion = canciones[-1]
    listToStr = ' '.join(map(str, cancion))
    with open("partitura.txt", 'w') as file:
        file.write(listToStr)
    for comp in range(len(cancion)):
        # playsound(waves[cancion[comp][0]], False)
        for note in range(len(cancion[comp][1])):
            notado_2(cancion[comp][1][note], cancion[comp][2][note], post)
            acord = AudioSegment.from_wav(f"sample{post}.wav")
            complete += acord
            os.remove(f"sample{post}.wav")
            post += 1

    complete.export("melody1.wav", format="wav")


# ---------------PANTALLA--------------------------------


window = Tk()
window.config(pady=20, padx=20)

window.title("The Melody Creator")
title = Label(text="The Melody Creator", font=("Arial", 24, "bold"))
title.grid(column=0, row=0, columnspan=3, pady=20)

choose_type = Label(text="Choose the type: ")
choose_type.grid(column=0, row=1)
opciones = ttk.Combobox()
opciones["values"] = ["alegre1", "alegre2", "alegre3", "epica"]
opciones.grid(column=1, row=1)

create_bt = Button(text="Create", command=componer)
create_bt.grid(column=0, row=2, pady=20)

play_bt = Button(text="Play Again", command=reproducir)
play_bt.grid(column=1, row=2)

save_bt = Button(text="Download", command=guardar)
save_bt.grid(column=2, row=2)

window.mainloop()
