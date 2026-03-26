class Timesheet:
    def __init__(self,timesheetId,shiftId, employeeId,totalHoursWorked):
        self.timesheetId= timesheetId
        self.shiftId= shiftId
        self.userId =userId
        self.totalHoursWorked =totalHoursWorked

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
