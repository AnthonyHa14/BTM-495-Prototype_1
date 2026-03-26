from User import User
class Employee(User):
    def __init__(self,userId: int,firstName: str, lastName: str, phoneNumber: str, email: str,password: str, dob: str,department: str,employmentStatus: str, hourlyRate: float):
        super().__init__(userId,firstName, lastName, phoneNumber,email,password,dob)
        self.department: str=department
        self.employmentStatus:  str= employmentStatus
        self.hourlyRate: float=hourlyRate
                     
# Select availability tab
    def selectAvailabilityTab(self):
        print("Availability tab selected")
        return True

 # Select schedule tab
    def selectScheduleTab(self):
        print("Schedule tab selected")
        return True
        
 # View assigned schedule
    def viewSchedule(self, scheduleId):
        print(f"Viewing schedule {scheduleId}")
        return scheduleId

# Confirm assigned shift
    def confirmSchedule(self, shiftId):
        print(f"Shift {shiftId} confirmed")
        return True

 # Give away shift
    def giveAwayShift(self, shiftId, scheduleId):
        print(f"Shift {shiftId} given away")
        return True

# Take available shift
    def takeAvailableShift(self, shiftId, scheduleId):
        print(f"Shift {shiftId} taken")
        return True


# Select availability
    def selectAvailability(self, shiftId):
        print(f"Availability selected for shift {shiftId}")
        return True

 # Validate employee info
    def submitForValidation(self):
        if self.firstName != "" and self.lastName != "":
            print("Employee validation successful")
            return True
        else:
            print("Employee validation failed")
            return False
            
 # Mark task complete
 def markTaskComplete(self, taskId, status):
        print(f"Task {taskId} marked {status}")
        return True

 # View timesheet
 def viewTimesheet(self):
        print("Viewing timesheet")
        return True

# View task list
    def viewTaskList(self, shiftId):
        print(f"Viewing task list for shift {shiftId}")
        return True

 # Create an incident form
    def createIncidentForm(self, userId, description):
        from Incident_Form import IncidentForm
        form = IncidentForm(1,userId,"2026-03-25", description, "pending")
        print("Incident form created.")
        return form
