## Messenger application. Basedd off PyMessenger by Tijndagamer
## Released under the MIT licence.
# You rock, man.

## Import stage.

try:
    from Notify import Main
    Notify = Main()
    Notify.SetMode("C")
    Notify.Success("Successfully imported Notify.")
except(ImportError):
    print("[!] Failed to import Notify.py")

try:
    from utilsv2 import Main as UtilsMain
    utils = UtilsMain()
    utils.SetDeviceEnvironment(0)
import socket
import time
import sys

class MessengerClient():
    def __init__(self):
        self.HostIP = ''
        self.Port = 5005
        self.BufferSize = 1024
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message = ""
        self.RecMessage = ""
    def Connect(self):
        Notify.Info("Connecting to '{}' ...".format(self.HostIP))
        self.sock.connect((self.HostIP, self.Port))

    def SendMessage(self):
        try:
            self.sock.send(self.message)
        except:
            Notify.Error("Unable to send message. ")

    def CheckForRecMessage(self):
        try:
            if self.RecMessage == "--LEFT--":
                Notify.Warning("Server disconnected. Terminating Connection.")
                self.sock.close()
        except:
            pass
        Notify.Cyan()
        print("({})> {}".format(self.HostIP, str(self.RecMessage)))

    def MPL(self):
        while True:
            print("""
        |------------------------------------------------------|
        |   {}:{}                              {}|
        |------------------------------------------------------|
            """.format(self.hour, self.minute, self.HostIP))
            self.message = input("[>] ")
            if self.message.upper() == "EXIT":
                self.sock.close()
                Notify.Error("Connection Closed.")
            else:
                self.SendMessage()
            self.CheckForRecMessage()

class MessengerServer():
    def __init__(self):
        self.__HostIP = ""
        self.__Port = 0
        self.__BufferSize = 1024

    def ConnectToServer(self):
