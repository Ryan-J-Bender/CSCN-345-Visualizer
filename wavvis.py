# CSCN 345 Final Project Sound Visualizer by Elshaddai Mekonnen, Tianna DeSouza, Ryan Bender 



# import matplotlib.pyplot as plt  
from scipy.io import wavfile as wav
import soundfile as sf
import numpy
import pygame as pg
import simpleaudio as sa
from pydub import AudioSegment

import WaveToRGB



# User input file name
filename = "cantinaband.wav"

# Pygame init
pg.init()
pg.mixer.init()

# Global Variables

FPS = 30
HEIGHT = 600
WIDTH = 1250
C = 299792458

# Display
display_surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Python .wav Visualizer")

color = (51, 79, 124)

fpsClock = pg.time.Clock()

# Conversion name
newfilename = "Cantinabund.wav"

# Convert Stereo to mono
sound = AudioSegment.from_wav(filename)
sound = sound.set_channels(1)
sound.export(newfilename, format="wav")


# Reads values into data list
data, rate = sf.read(newfilename)

# Convert to int array ant resize array
data = numpy.array(data)
data = data.astype(int)


for i in data:
    if i % 1470 != 0:
        data = numpy.delete(data, i)

for i in data:

    data[i] = data[i] * 1000

    if data[i] < 1:
        data[i] = 1
    

numpy.round(data, 0)



# Prints info
print ("The sample rate is " + str(rate) + " samples per second")

print ("There are " + str(len(data)) + " samples.")

print ("Then the audio length is: " + str(len(data) / rate) + " seconds.")

# Plays audio
pg.mixer.music.load(newfilename)
pg.mixer.music.set_volume(100.0)
pg.mixer.music.play()

loop = True

display_surface.fill(color)
pg.display.update()

# iterator
i = 0

# game loop
while loop == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    
    red = (WaveToRGB.wav_to_redgb(data[i]))
    green = (WaveToRGB.wav_to_rgreenb(data[i]))
    blue = (WaveToRGB.wav_to_rgblue(data[i]))


    color = (red, green, blue)
    display_surface.fill(color)
    pg.display.update()

    fpsClock.tick(FPS)

    i += 1

pg.quit()
