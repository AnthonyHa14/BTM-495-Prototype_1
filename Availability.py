class Availability:
    
    def __init__(self,availabilityId: int,userId: int,date: str,startTime: int,endTime: int,status: str):
        self.availabilityId: int = availabilityId
        self.userId: int=userId
        self.date: str =date
        self.startTime: int= startTime
        self.endTime: int =endTime
        self.status: str =status

  # Create a new availability entry
    def createAvailability(self, date, startTime, endTime):
        availability = Availability(self.availabilityId,self.userId,date,startTime,endTime,"pending")
        print("Availability successfully created")
        return availability

#Validate the availability information
    def validateAvailability(self):
        if self.date != "" and self.startTime != "" and self.endTime != "":
            print("Availability is valid")
            return True
        else:
            print("Please fill out missing information")
            return False
            
 #Get the shift details
    def getShiftDetails(self, shiftId,shiftDayOfWeek,shiftStartTime, shiftEndTime):
        details = f"Shift {shiftId}: Day {shiftDayOfWeek}, {shiftStartTime} - {shiftEndTime}"
        print(details)
        return details

 #Submit the availability
    def submitAvailability(self):
        if self.validateAvailability():
            self.status = "submitted"
            print("Availability sucessfully submitted")
            return True
        else:
            print("Availability submission failed")
            return False

#Update the availability
    def updateAvailability(self, date, startTime, endTime):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        print("Availability successfully updated")
        return True

#Save the availability
    def saveAvailability(self):
        print("Availability successfully saved")
        return True

#View the availability details
    def viewAvailability(self):
        details = f"Availability {self.availabilityId}: {self.date}, {self.startTime} - {self.endTime}"
        print(details)
        return details
