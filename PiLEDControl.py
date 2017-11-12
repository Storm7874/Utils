import os

class Indicator:
    def __init__(self):
        self.LEDdir = "> /sys/class/leds/led1"

    def IndicatorOn(self):
        os.system("echo 255 " + self.LEDdir)

    def IndicatorOff(self):
        os.system("echo 0 " + self.LEDdir)

