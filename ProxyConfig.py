try:
    from Notify import Main
    Notify = Main()
    Notify.SetMode("C")
except(ImportError):
    print("Failed to import Notify.")

class Main():
    def __init__(self):
        self.host = ""
        self.port = 0
        self.user = ""
        self.psw = ""
        self.hash = ""
        self.psarray = []
        self.msk = ""

    def GetNewData(self):
        while True:
            try:
                self.host = input("[Host]> ")
                if len(self.host) > 15:
                    Notify.Error("Incorrect Host.")
                else:
                    break
            except(ValueError):
                Notify.Error("Incorrect Host.")
        while True:
            try:
                self.port = int(input("[Port]> "))
                if self.port < 0 or self.port > 65535:
                    Notify.Error("Incorrect Port")
                else:
                    break
            except(ValueError):
                Notify.Error("Incorrect Port.")
        while True:
            try:
                self.user = input("[User]> ")
                break
            except(ValueError):
                Notify.Error("Invalid Username.")
        while True:
            try:
                self.psw = input("[Psw]> ")
                break
            except(ValueError):
                Notify.Error("Invalid Password.")
        self.MaskPassword()

        print("Collected Data: ({}/{})@{}:{}".format(self.user, self.psw, self.host, self.port))

    def MaskPassword(self):
        self.psarray.append(self.psw)
        for count in range(0, len(self.psarray)):
            if (len(self.psarray)) - count < 3:
                print(count)
                print(self.psarray[count])
                print(self.psw[count])
                self.psarray[count] = self.psw[count]
            else:
                self.psarray[count] = "*"
            self.msk = str(self.psarray)



Core = Main()
Core.GetNewData()
Core.MaskPassword()



