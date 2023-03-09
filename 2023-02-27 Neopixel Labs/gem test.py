import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True: 
    pixels.fill((0,0,0))
    pixels[0]=(128,246,253) #sets light blue (diamond)
    pixels[1]=(128,246,253)
    pixels[2]=(128,246,253)
    pixels[3]=(128,246,253)
    pixels[4]=(128,246,253)