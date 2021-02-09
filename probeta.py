import sounddevice as sd
from scipy.io.wavfile import write
import winsound
import canciones_buenas as cb
from playsound import playsound

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


'''
fs = 44100  # Sample rate
seconds = 12  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
cb.reproducir(cancion1)
sd.wait()  # Wait until recording is finished
write('output2.wav', fs, myrecording)  # Save as WAV file
'''

import numpy as nup
from scipy.io.wavfile import write, read
from pydub import *
#from ffmpeg import *
import os
import song_creator as sc

sps = 44100
vol = 0.3


'''
acorde1 = AudioSegment.from_wav("sample1.wav")
acorde2 = AudioSegment.from_wav("sample2.wav")

combined = AudioSegment.empty()
combined += acorde1
combined += acorde2
combined += acorde1

combined.export("combined.wav", format="wav")
os.remove("sample1.wav")
os.remove("sample2.wav")

playsound("combined.wav")
'''


def notado_2(nota, figur, post):
    n_final = sonidos[nota]
    time = duracion[figur]
    esm = nup.arange(time/1000 * sps)
    wf1 = nup.sin(2 * nup.pi * esm * n_final / sps) * vol
    wf_int1 = nup.int16(wf1 * 32767)
    write(f"sample{post}.wav", sps, wf_int1)



def guardar():
    complete = AudioSegment.empty()
    post = 0
    cancion= sc.canciones[-1]
    for comp in range(len(cancion)):
        #playsound(waves[cancion[comp][0]], False)
        for note in range(len(cancion[comp][1])):
             notado_2(cancion[comp][1][note], cancion[comp][2][note], post)
             acord = AudioSegment.from_wav(f"sample{post}.wav")
             complete += acord
             os.remove(f"sample{post}.wav")
             post += 1


    complete.export("melody1.wav", format="wav")
