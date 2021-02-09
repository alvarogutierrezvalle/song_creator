figuras ={'b':2,'np':1.5,'n':1,'c':0.5,'s':0.25}
duracion ={'b':1200,'np':900,'n':600,'c':300,'s':150}
notas =('do','re','mi','fa','sol','la','si')
primera_nota={'DoM':('do','mi','sol'),'SolM':('re','si','sol'),'FaM':('do','fa','la'),'Lam':('do','mi','la')}
last_compas=['Do', ['do'], ['b']]
sonidos={'do':261,'re':293,'mi':329,'fa':349,'sol':392,'la':440,'si':494}
#Añadir sucesiones tipicas de acordes
secuencias=[('DoM','SolM','FaM','SolM','DoM','SolM','FaM','SolM'),('DoM','DoM','SolM','SolM','FaM','FaM','SolM','SolM'),('DoM','Lam','FaM','SolM','DoM','Lam','FaM','SolM')]

waves = {
    'Do': 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\Do.wav',
    'DoM' : 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\DoM.wav',
    'SolM' : 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\SolM.wav',
    'FaM' : 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\FaM.wav',
    'Lam' : 'D:\\Documentos\\Partituras\\Notas\\Notas wav\\Lam.wav'
}


import random
import winsound
from playsound import playsound
import song_creator as scr

def notado(nota, figur):
    n_final = sonidos[nota]
    time = duracion[figur]
    return winsound.Beep(n_final, time)


def reproducir(cancion):
    for comp in range(len(cancion)):
        playsound(waves[cancion[comp][0]], False)
        for note in range(len(cancion[comp][1])):
            notado(cancion[comp][1][note], cancion[comp][2][note])



cancion1=[
['DoM', ['mi', 'si', 're', 'fa'], ['n', 's', 'c', 's']],


['SolM', ['re', 'do'], ['np', 'c']],


['FaM', ['la'], ['b']],


['SolM', ['re', 'sol'], ['c', 'np']],


['DoM', ['mi', 'la', 'la', 'fa', 'mi', 're'], ['c', 's', 'c', 's', 's', 's']],


['SolM', ['re', 'mi', 'fa'], ['np', 's', 's']],


['FaM', ['do'], ['b']],


['SolM', ['sol'], ['b']],


['Do', ['do'], ['b']]
]

cancion2=[
['DoM', ['mi'], ['b']],


['Lam', ['la'], ['b']],


['FaM', ['la'], ['b']],


['SolM', ['sol'], ['b']],


['DoM', ['mi'], ['b']],


['Lam', ['do', 'do', 'si'], ['np', 's', 's']],


['FaM', ['fa'], ['b']],


['SolM', ['si', 're'], ['np', 'c']],


['Do', ['do'], ['b']]

]

#reproducir(cancion2)

