from datetime import datetime
import time
import os


class Alarm:
        def __init__(self,name):

                self.name = names
                self.time = datetime.now()

        def viewTime(self):
        """This function fetches and displays the current time to the user"""
            displayTime = self.time.strftime("%H:%M")
            print("The time is: ",displayTime)


        def setTime(self):
        """This functions allows the user to change the time to a new time. It takes no parameteres and prints out the new set time."""
            hrs = eval(input("Enter hour: "))
            mins = eval(input("Enter minute: "))
            if hrs<24 and hrs>0 and mins<60 and mins>0:
                    newTime = self.time.replace(hour=hrs, minute=mins).strftime("%H:%M")
                    self.time = newTime
                    print("Time succesfully set\nThe time is: ",self.time)
            else:
                    print("Invalid time entered")
    
                    