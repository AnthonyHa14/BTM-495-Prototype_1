class Timesheet:
    def __init__(self, timesheetId: int,shiftId: int,userId: int,totalHoursWorked: float):    
        self.timesheetId:int = timesheetId
        self.shiftId: int =shiftId
        self.userId:int =userId
        self.totalHoursWorked:float =totalHoursWorked

#Calculate total hours worked
    def calculateTotalHours(self):
        print("Total hours worked:", self.totalHoursWorked)
        return self.totalHoursWorked

#Update total worked hours
    def updateHours(self, totalHoursWorked):
        self.totalHoursWorked = totalHoursWorked
        print("Hours successfully updated")
        return True

# Submit the timesheet to payroll
    def submitToPayroll(self):
        if self.totalHoursWorked > 0:
            print("Timesheet successfully submitted to payroll ")
            return True
        else:
            print("Timesheet submission failed")
            return False

# Verify timesheet details
    def verifyTimesheetDetails(self):
        details = f"Timesheet {self.timesheetId}, Hours: {self.totalHoursWorked}"
        print(details)
        return details
