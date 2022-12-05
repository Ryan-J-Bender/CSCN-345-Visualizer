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


data = [abs(i * 1000) for i in data]
data = numpy.array(data)
data = data.astype(int)

for i in data:
    
    if data[i] == 0:
        data[i] = 1

for i in data:
    if i % 9 != 0:
        data = numpy.delete(data, i)


# Prints info
print ("The sample rate is " + str(rate) + " samples per second")

print ("There are " + str(len(data)) + " samples.")

print ("Then the audio length is: " + str(len(data) / rate) + " seconds.")


# for j in data:
#     data[j] = int(data[j])




# Prints data and graph
# # print(fixeddata)

# # plt.plot(fixeddata)

# # plt.show()

# # print(fixeddata.max())
# # print(fixeddata.min())

# Plays audio
pg.mixer.music.load(newfilename)
pg.mixer.music.set_volume(100.0)
pg.mixer.music.play()

loop = True

display_surface.fill(color)
pg.display.update()

# iterator
i = 0

print(data)

# # # game loop
# # while loop == True:
# #     for event in pg.event.get():
# #         if event.type == pg.QUIT:
# #             loop = False
    
# #     red = (WaveToRGB.wav_to_rgb(data[i], 0))
# #     green = (WaveToRGB.wav_to_rgb(data[i], 1))
# #     blue = (WaveToRGB.wav_to_rgb(data[i], 2))

# #     print(red)
# #     print(green)
# #     print(blue)


# #     color = (red, green, blue)
# #     display_surface.fill(color)
# #     pg.display.update()

# #     fpsClock.tick(FPS)

# #     i += 1

pg.quit()

