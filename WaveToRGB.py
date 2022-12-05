#static private final double Gamma = 0.80
#static private final double IntensityMax = 255

# * Taken from Earl F. Glynn's web page:
 #* <a href="http://www.efg2.com/Lab/ScienceAndEngineering/Spectra.htm">Spectra Lab Report</a>

import math

#Change Var to be static private and final but python version
def wav_to_redgb(x):
    Gamma = 0.80
    IntensityMax = 255
        
    factor = 0
    Red = 0 
    Green = 0 
    Blue = 0
    c = 299792458

    Wavelength = c / x

    if (Wavelength >= 380) and (Wavelength < 440):
        Red = -(Wavelength - 440) / (440 - 380)
        Green = 0.0
        Blue = 1.0
    

    elif ((Wavelength >= 440) and (Wavelength < 490)):
        Red = 0.0
        Green = (Wavelength - 440) / (490 - 440)
        Blue = 1.0
    
    elif((Wavelength >= 490) and (Wavelength < 510)): 
        Red = 0.0
        Green = 1.0
        Blue = -(Wavelength - 510) / (510 - 490)

    elif((Wavelength >= 510) and (Wavelength < 580)):
        Red = (Wavelength - 510) / (580 - 510)
        Green = 1.0
        Blue = 0.0

    elif((Wavelength >= 580) and (Wavelength < 645)):
        Red = 1.0
        Green = -(Wavelength - 645) / (645 - 580)
        Blue = 0.0

    if((Wavelength >= 645) and (Wavelength < 781)):
        Red = 1.0
        Green = 0.0
        Blue = 0.0
    else:
        Red = 0.0
        Green = 0.0
        Blue = 0.0

    # Let the intensity fall off near the vision limits

    if((Wavelength >= 380) and (Wavelength < 420)):
            factor = 0.3 + 0.7 * (Wavelength - 380) / (420 - 380)

    elif((Wavelength >= 420) and (Wavelength < 701)):
            factor = 1.0

    elif((Wavelength >= 701) and (Wavelength < 781)):
            factor = 0.3 + 0.7 * (780 - Wavelength) / (780 - 700)
    else:
        factor = 0.0
        
    #int[] rgb = new int[3]
    rgb = [0, 0, 0] #1D array
    #do we need a 3D array??? for RGB

    #Don't want 0^x = 1 for x <> 0
    #Red
    rgb[0] = Red 
    if (Red == 0.0):
        Red = 0
    else:
        Red = (IntensityMax * math.pow(Red * factor, Gamma) + .5)
        
    rgb[1] = Green 
    if (Green == 0.0):
        Green = 0
    else:
        Green = (IntensityMax * math.pow(Green * factor, Gamma) + .5)

    rgb[0] = Blue
    if (Blue == 0.0):
        Blue = 0
    else:
        Blue = (IntensityMax * math.pow(Blue * factor, Gamma) + .5)

    rgb = [Red, Green, Blue]


    return rgb[0]

def wav_to_rgreenb(x):
    Gamma = 0.80
    IntensityMax = 255
        
    factor = 0
    Red = 0 
    Green = 0 
    Blue = 0
    c = 299792458

    Wavelength = c / x

    if (Wavelength >= 380) and (Wavelength < 440):
        Red = -(Wavelength - 440) / (440 - 380)
        Green = 0.0
        Blue = 1.0
    

    elif ((Wavelength >= 440) and (Wavelength < 490)):
        Red = 0.0
        Green = (Wavelength - 440) / (490 - 440)
        Blue = 1.0
    
    elif((Wavelength >= 490) and (Wavelength < 510)): 
        Red = 0.0
        Green = 1.0
        Blue = -(Wavelength - 510) / (510 - 490)

    elif((Wavelength >= 510) and (Wavelength < 580)):
        Red = (Wavelength - 510) / (580 - 510)
        Green = 1.0
        Blue = 0.0

    elif((Wavelength >= 580) and (Wavelength < 645)):
        Red = 1.0
        Green = -(Wavelength - 645) / (645 - 580)
        Blue = 0.0

    if((Wavelength >= 645) and (Wavelength < 781)):
        Red = 1.0
        Green = 0.0
        Blue = 0.0
    else:
        Red = 0.0
        Green = 0.0
        Blue = 0.0

    # Let the intensity fall off near the vision limits

    if((Wavelength >= 380) and (Wavelength < 420)):
            factor = 0.3 + 0.7 * (Wavelength - 380) / (420 - 380)

    elif((Wavelength >= 420) and (Wavelength < 701)):
            factor = 1.0

    elif((Wavelength >= 701) and (Wavelength < 781)):
            factor = 0.3 + 0.7 * (780 - Wavelength) / (780 - 700)
    else:
        factor = 0.0
        
    #int[] rgb = new int[3]
    rgb = [0, 0, 0] #1D array
    #do we need a 3D array??? for RGB

    #Don't want 0^x = 1 for x <> 0
    #Red
    rgb[0] = Red 
    if (Red == 0.0):
        Red = 0
    else:
        Red = (IntensityMax * math.pow(Red * factor, Gamma) + .5)
        
    rgb[1] = Green 
    if (Green == 0.0):
        Green = 0
    else:
        Green = (IntensityMax * math.pow(Green * factor, Gamma) + .5)

    rgb[0] = Blue
    if (Blue == 0.0):
        Blue = 0
    else:
        Blue = (IntensityMax * math.pow(Blue * factor, Gamma) + .5)

    rgb = [Red, Green, Blue]


    return rgb[1]


def wav_to_rgblue(x):
    Gamma = 0.80
    IntensityMax = 255
        
    factor = 0
    Red = 0 
    Green = 0 
    Blue = 0
    c = 299792458

    Wavelength = c / x

    if (Wavelength >= 380) and (Wavelength < 440):
        Red = -(Wavelength - 440) / (440 - 380)
        Green = 0.0
        Blue = 1.0
    

    elif ((Wavelength >= 440) and (Wavelength < 490)):
        Red = 0.0
        Green = (Wavelength - 440) / (490 - 440)
        Blue = 1.0
    
    elif((Wavelength >= 490) and (Wavelength < 510)): 
        Red = 0.0
        Green = 1.0
        Blue = -(Wavelength - 510) / (510 - 490)

    elif((Wavelength >= 510) and (Wavelength < 580)):
        Red = (Wavelength - 510) / (580 - 510)
        Green = 1.0
        Blue = 0.0

    elif((Wavelength >= 580) and (Wavelength < 645)):
        Red = 1.0
        Green = -(Wavelength - 645) / (645 - 580)
        Blue = 0.0

    if((Wavelength >= 645) and (Wavelength < 781)):
        Red = 1.0
        Green = 0.0
        Blue = 0.0
    else:
        Red = 0.0
        Green = 0.0
        Blue = 0.0

    # Let the intensity fall off near the vision limits

    if((Wavelength >= 380) and (Wavelength < 420)):
            factor = 0.3 + 0.7 * (Wavelength - 380) / (420 - 380)

    elif((Wavelength >= 420) and (Wavelength < 701)):
            factor = 1.0

    elif((Wavelength >= 701) and (Wavelength < 781)):
            factor = 0.3 + 0.7 * (780 - Wavelength) / (780 - 700)
    else:
        factor = 0.0
        
    #int[] rgb = new int[3]
    rgb = [0, 0, 0] #1D array
    #do we need a 3D array??? for RGB

    #Don't want 0^x = 1 for x <> 0
    #Red
    rgb[0] = Red 
    if (Red == 0.0):
        Red = 0
    else:
        Red = (IntensityMax * math.pow(Red * factor, Gamma) + .5)
        
    rgb[1] = Green 
    if (Green == 0.0):
        Green = 0
    else:
        Green = (IntensityMax * math.pow(Green * factor, Gamma) + .5)

    rgb[0] = Blue
    if (Blue == 0.0):
        Blue = 0
    else:
        Blue = (IntensityMax * math.pow(Blue * factor, Gamma) + .5)

    rgb = [Red, Green, Blue]


    return rgb[2]