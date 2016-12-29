# Coordinates are based on 1920x1080 resolution
# with Chrome shifted to left half of screen

import pyscreenshot as ImageGrab
import os
import time

padding = { 'x': 20, 'y': 250 }
width = 639
height = 480

# def filename():
    # return 'full_snap__' + str(int(time.time())) + '.png'

def screenGrab():
    box = (padding['x'], padding['y'], padding['x'] + width, padding['y'] + height)
    image = ImageGrab.grab(box, backend='mac_screencapture')
    return image

# def main():
    # screenGrab()

# if __name__ == '__main__':
    # main()
