import os
import time
import datetime

class Timer:
    def __init__(self, StartHour, EndHour, Name, Pin):
        self.StartHour = StartHour
        self.EndHour = EndHour
        self.Name = Name
        self.Active = False
        self.CurrentHour = 0
        self.TimerLoop()


    def GetNewTime(self):
        self.CurrentHour = datetime.datetime.today().hour
        self.CurrentHour = int(self.CurrentHour)

    def CheckIfTimerActive(self):
        if self.CurrentHour >= self.StartHour:
            if self.CurrentHour < self.EndHour:
                self.Active = True
        else:
            self.Active = False

    def IsTimerActive(self):
        if self.Active == True:
            return True
        else:
            return False

    def TimerLoop(self):
        self.GetNewTime()
        self.CheckIfTimerActive()

MainDeviceList = [["EFSS","00:0C:76:4E:1A:D1","192.168.1.25"],
                  ["SGPS","78:45:C4:04:9D:68","192.168.1.3"]
                  ]
# [[dev_name, Mac, IP]]
# [["EFSS","XX:XX:XX:XX:XX","XXX.XXX.XXX.XXX"],...]

class Main:
    def __init__(self):
        self.CurrentHour = 0
        self.CurrentMinute = 0

    def StartAllDevices(self):
        for count in range(0, len(MainDeviceList)):
            os.system("etherwake " + MainDeviceList[count][1])
            print("Packet Sent to: {}".format(MainDeviceList[count][1]))


    def PrintDeviceStatus(self):
        pass

    def AutoMode(self):
        pass

    def MainMenu(self):
        print("""
        |----------------------------------|
        | Current Time: {}:{}              |
        |----------------------------------|
        |[1] Start All Devices             |
        |[2] Print Device Status           |
        |[3] Automatic Mode                |
        |[4] Exit                          |
        |----------------------------------|
        """.format(self.CurrentHour, self.CurrentMinute))
        while True:
            try:
                menuchoice = int(input("> "))
                if menuchoice not in [1,2,3,4]:
                    menuchoice = int(input("> "))
                else:
                    break
            except(ValueError):
                menuchoice = int(input("> "))
        if menuchoice == 1:
            self.StartAllDevices()
        elif menuchoice == 2:
            self.PrintDeviceStatus()
        elif menuchoice == 3:
            self.AutoMode()
        elif menuchoice == 4:
            exit()

Core = Main()
Core.MainMenu()