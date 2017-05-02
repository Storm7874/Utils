import os
import time
import platform

class Main():
    def __init__(self):
        self.Platform = ""
    def GetWorkingPlatform(self):
        if platform.system() == "linux":
            self.Platform = "L"
        else:
            self.Platform = "W"

Initiate = Main()
Initiate.GetWorkingPlatform()


class Loading():
    def __init__(self):
        self.MaxValue = 10
        self.Initial = 0
        self.Step = 0
        self.BarCore = []
        self.DrawUpper = []
        self.DrawLower = []
        self.Iterat = 0
    def DrawSkeleton(self):
        print("""
        |{}|
        |{}|
        |{}|
        """.format(self.DrawUpper, self.BarCore, self.DrawLower))

    def Update(self):
        if len(self.DrawLower) == self.MaxValue:
            pass
        else:
            self.DrawLower.append("-")
        if len(self.BarCore) == self.MaxValue:
            pass
        else:
            self.BarCore.append("#")
        if len(self.DrawLower) == self.MaxValue:
            pass
        else:
            self.DrawLower.append("-")

Loader = Loading()
while True:
    Loader.DrawSkeleton()
    input()
    Loader.Update()
