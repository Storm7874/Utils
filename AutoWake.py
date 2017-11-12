import os
import time
import datetime
try:
    from Notify import Main as NotifyMain
    Notify = NotifyMain()
    Notify.SetMode("C")
except(ImportError):
    print("Unable to import Notify, Aborting.")
    exit()

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

MainDeviceList = [["EFSS","00:0C:76:4E:1A:D1","192.168.1.25","OFFLINE"],
                  ["SGPS","78:45:C4:04:9D:68","192.168.1.3","OFFLINE"]
                  ]
# [[dev_name, Mac, IP]]
# [["EFSS","XX:XX:XX:XX:XX","XXX.XXX.XXX.XXX","OFFLINE/ONLINE"],...]

class Main:
    def __init__(self):
        self.CurrentHour = 0
        self.CurrentMinute = 0

    def GetNewTimeData(self):
        self.CurrentHour = datetime.datetime.today().hour
        self.CurrentMinute = datetime.datetime.today().minute

    def StartAllDevices(self):
        for count in range(0, len(MainDeviceList)):
            os.system("etherwake " + MainDeviceList[count][1])
            print("Packet Sent to: {}".format(MainDeviceList[count][1]))
        self.MainMenu()

    def ScanDevices(self):
        Notify.Info("Scanning Devices...")
        for count in range(0, len(MainDeviceList)):
            response = os.system("ping -c 1" + MainDeviceList[count][2])
            if response == 0:
                MainDeviceList[count][3] == "ONLINE"
            else:
                MainDeviceList[count][3] == "OFFLINE"


    def PrintDeviceStatus(self):
        self.ScanDevices()
        for count in range(0, len(MainDeviceList)):
            print("Device: " + MainDeviceList[count][0])
            if MainDeviceList[count][3] == "ONLINE":
                Notify.Green()
                print("ONLINE")
                Notify.ClearColour()
            elif MainDeviceList[count][3] == "OFFLINE":
                Notify.Red()
                print("OFFLINE")
                Notify.ClearColour()
            print()


    def AutoMode(self):
        pass

    def MainMenu(self):
        os.system("clear")
        self.GetNewTimeData()
        self.ScanDevices()
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
        self.MainMenu()

Core = Main()
Core.MainMenu()