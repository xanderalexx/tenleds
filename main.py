import RPi.GPIO as g
import time
import config.config as config

led1 = config.led1
led2 = config.led2
led3 = config.led3
led4 = config.led4
led5 = config.led5
led6 = config.led6
led7 = config.led7
led8 = config.led8
led9 = config.led9
led10 = config.led10

allleds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10]

g.setmode(g.BCM)
g.setup(allleds, g.OUT)
g.output(allleds, g.LOW)

def setleds(x):
    i = 0
    for y in allleds:
        if x > i:
            g.output(allleds[i], g.HIGH)
        else:
            pass
        i += 1