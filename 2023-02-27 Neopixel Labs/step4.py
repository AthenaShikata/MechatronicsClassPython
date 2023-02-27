# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT


"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel
# Calls the circuit Python neopixel library, specifies the default board
# pins for the Neopixels, and the number of neopixels to access.  Returns a
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    # indexes the first element of the 'pixels' list and points to the
    # # first 10 Neopixels in the 'pixels' list
    pixels[1] #black
    pixels[2] #grey
    pixels[3] #white
    pixels[4] #light purple
    pixels[5] #purple

    pixels[6] #black
    pixels[7] #grey
    pixels[8] #white
    pixels[9] #light green
    pixels[10] #green


    """
    pixels[0]=(255, 0, 0)
    pixels[1]=(0, 255, 0)
    pixels[2]=(0, 0, 255)
    time.sleep(0.5) #delay equivalent
    pixels.fill((0, 0, 0)) #writes the Neopixels to off
    time.sleep(0.5)
    """