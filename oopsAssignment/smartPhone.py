class SmpartPhone():
    def __init__(self,battery):
        self.battery=battery

    def _check_Battrary(self):
        if self.battery>20:
            print("battery is charged")
        else:
            print("battery is low! plase charge it.")

    def make_call(self):
        self._check_Battrary()
        print("call is being made.. ")


phone1 = SmpartPhone(80)
phone1._check_Battrary() 
phone1.make_call()