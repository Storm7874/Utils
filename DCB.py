## Simple script to send/receive morse data through audio link connected to radio.
## On/Off variable controlled by relay
import platform
import time
try:
    from Notify import Main as NotifyMain
    Notify = NotifyMain()
    Notify.SetMode("A")
    Notify.Success("Notify Imported.")
except(ImportError):
    print("Unable to import notify. Aborting.")
    exit()

try:
    from utilsv2 import Main as UtilsMain
    utils = UtilsMain()
    if platform.system() == "linux":
        utils.SetDeviceEnvironment(1)
    else:
        utils.SetDeviceEnvironment(0)
except(ImportError):
    Notify.Error("Failed to import Utils.")
    exit()


try:
    import RPi.GPIO as GPIO
    Notify.Success("Imported GPIO modules")
    GPIOstate = True
except(ImportError):
    Notify.Error("Failed to import GPIO modules.")
    GPIOstate = False
    Notify.Warning("Attempting to import eGPIO modules.")
    try:
        from EmulatorGUI import GPIO
        Notify.Success("Successfully imported eGPIO modules")
    #except(ImportError):
        Notify.Error("Failed to import eGPIO modules. Aborting.")
        exit()



MorseDict = [["A",".","-"],
            ["B","-",".",".","."],
            ["C","-",".","-","."],
            ["D","-",".","."],
            ["E","."],
            ["F",".",".","-","."],
            ["G","-","-","."],
            ["H",".",".",".","."],
            ["I",".","."],
            ["J",".","-","-","-"],
            ["K","-",".","-"],
            ["L",".","-",".","."],
            ["M","-","-"],
            ["N","-","."],
            ["O","-","-",],
            ["P",".","-","-","."],
            ["Q","-","-",".","-"],
            ["R",".","-","."],
            ["S",".",".","."],
            ["T","-"],
            ["U",".",".","-"],
            ["V",".",".",".","-"],
            ["W",".","-","-"],
            ["X","-",".",".","-"],
            ["Y","-",".","-","-"],
            ["Z","-","-",".","."]]

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

class HardwareControl():
    def __init__(self):
        self.Coil1 = 0
        self.Coil2 = 0
        self.StatusLED = 0
        self.Message = ""
        self.PlainText = []
        self.Encoded = []
        self.Dot = 0.5
        self.Dash = 1.5
        self.CurrentValue = ""



    def CoilOneEnergize(self):
        GPIO.output(self.Coil1, GPIO.LOW)

    def CoilOneDeenergize(self):
        GPIO.output(self.Coil1, GPIO.HIGH)


    def CoilTwoEnergize(self):
        GPIO.output(self.Coil2, GPIO.LOW)

    def CoilTwoDeenergize(self):
        GPIO.output(self.Coil2, GPIO.HIGH)



class Encode(HardwareControl):
    def __init__(self):
        self.Message = ""
        self.PlainText = []
        self.Encoded = []
        self.Dot = 0.5
        self.Dash = 1.5
        self.CurrentValue = ""
        self.Coil1 = 24
        self.Coil2 = 26

    def SetupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.Coil1, GPIO.OUT)
        GPIO.setup(self.Coil2, GPIO.OUT)
        GPIO.setup(self.Coil1, GPIO.HIGH)
        GPIO.setup(self.Coil2, GPIO.HIGH)

    def GetMessageData(self):
        Notify.Green()
        print("Please enter the message to send")
        self.Message = input(">> ")
        Notify.ClearColour()
        self.PlainText.append(list(self.Message))
        #print(self.PlainText)

    def ConvertMessageToMorse(self):
        for char in self.Message:
            self.Encoded.append(CODE[char.upper()])
        #print(self.Encoded)

    def Transmit(self):
        for count in range(0,len(self.Encoded)):
            self.CurrentValue = self.Encoded[count]
            for count in range(0,len(self.CurrentValue)):
                if self.CurrentValue[count] == ".":
                    self.CoilOneEnergize()
                    time.sleep(self.Dot)
                    self.CoilOneDeenergize()
                elif self.CurrentValue[count] == "-":
                    self.CoilOneEnergize()
                    time.sleep(self.Dash)
                    self.CoilOneDeenergize()





Coder = Encode()
Coder.SetupGPIO()
Coder.GetMessageData()
Coder.ConvertMessageToMorse()
Coder.Transmit()

