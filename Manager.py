from User import User

class Manager(User):
    def __init__(self,userId: int, firstName: str,  lastName: str,phoneNumber: str,email: str,password: str, dob: str,department: str,employmentStatus: str,hourlyRate: float):

        super().__init__(userId, firstName,lastName, phoneNumber,email,password,dob)
        self.department:str =department
        self.employmentStatus:str=employmentStatus
        self.hourlyRate float=hourlyRate
                     
#Create schedule draft
    def createScheduleDraft(self, shiftId, scheduleId, userId):
        print("Schedule draft created.")
        return True
        
 # Publish schedule
    def publishSchedule(self, scheduleId, userId):
        print("Schedule published.")
        return True

#Create message text
    def createMessage(self, message):
        print("Message created.")
        return message

# Select employees
    def selectEmployees(self, userId):
        print(f"Employee {userId} selected.")
        return True
        
#Send notification
    def sendNotification(self, message):
        notification = Notification( 1, message,self.userId,"sent","2026-03-25")
        print("Notification sent.")
        return notification

# Approve shift change
    def approveShiftChanges(self, shiftId, userId):
        print("Shift change approved.")
        return True

 # Approve timesheet
    def approveTimesheet(self, timesheetId):
        print("Timesheet approved.")
        return True
