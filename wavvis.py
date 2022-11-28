# CSCN 345 Final Project Sound Visualizer by Elshaddai Mekonnen, Tianna DeSouza, Ryan Bender 



import matplotlib.pyplot as plt  
from scipy.io import wavfile as wav
import soundfile as sf
import numpy
import pygame as pg
import simpleaudio as sa
from pydub import AudioSegment



# User input file name
filename = "cantinaband.wav"

# Pygame init
pg.init()

# Global Variables

HEIGHT = 600
WIDTH = 1250
c = 299792458

# Conversion name
newfilename = "Cantinabund.wav"

# Convert Stereo to mono
sound = AudioSegment.from_wav(filename)
sound = sound.set_channels(1)
sound.export(newfilename, format="wav")


# Reads values into data list
data, rate = sf.read("Cantinabund.wav")


# Prints info
print ("The sample rate is " + str(rate) + " samples per second")

print ("There are " + str(len(data)) + " samples.")

print ("Then the audio length is: " + str(len(data) / rate) + " seconds.")


# # # Prints data and graph
# # print(data)

# # plt.plot(data)

# # plt.show()

# for i in data:

#     if ( == 0):
#          += 0.0000000000000001
#     wavelength = ( c / (data[:, 0])[i] )

# for i in data:
#     print(data[i])


print(data.max())
print(data.min())
# Plays audio
wav_obj = sa.WaveObject.from_wave_file("Cantinabund.wav")
play_obj = wav_obj.play()
play_obj.wait_done()
