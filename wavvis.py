# CSCN 345 Final Project Sound Visualizer by Elshaddai Mekonnen, Tianna DeSouza, Ryan Bender 

import matplotlib.pyplot as plt  
from scipy.io import wavfile as wav
import numpy
import pygame as pg
import sounddevice as sd
import soundfile as sf

filename = "cantinaband.wav"

data, fs = sf.read(filename, dtype='float32')

sd.play(data, fs)
status = sd.wait()

pg.init()

HEIGHT = 600
WIDTH = 1250


display = pg.display.setmode(WIDTH, HEIGHT)

rate, data = wav.read(filename)

print ("The sample rate is " + str(rate) + " samples per second")

print ("There are " + str(len(data)) + " samples.")

print ("Then the audio length is: " + str(len(data) / rate) + " seconds.")

print (data)

plt.plot(data)

plt.show()
