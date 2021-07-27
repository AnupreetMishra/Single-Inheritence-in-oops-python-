class Phone:
    def __init__(self):
     pass
  
  
    def dial(self,number):
      print("Calling the number ",number)
  
  
    def sms(self,number):
      print("Sending SMS to ",number)


class SmartPhone(Phone):
    def __init__(self):
      Phone.__init__(self)

    def internet(self):
      print("Surfing Internet")

    def camera(self):
      print("Camera is on")


samsung=Phone()

oneplus=SmartPhone()

samsung.dial(8933026609)

oneplus.dial(8933026609)
     