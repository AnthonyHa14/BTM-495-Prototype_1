class Schedule:
    def __init__(self, shiftId, shiftDayOfWeek,shiftStartTime,shiftEndTime):
        self.shiftId = shiftId
        self.shiftDayOfWeek = shiftDayOfWeek
        self.shiftStartTime = shiftStartTime
        self.shiftEndTime = shiftEndTime

 # Save the schedule as a draft
    def saveScheduleDraft(self):
        self.scheduleStatus = "draft"
        print("Schedule draft saved.")
        return True
        
# Save the schedule as published
    def savePublishedSchedule(self):
        self.scheduleStatus = "published"
        print("Schedule published.")
        return True

 # Validate if there is enough shift coverage
    def validatesShiftCoverage(self):
        if self.totalEmployeesPerDay > 0:
            print("Shift coverage valid.")
            return True
        else:
            print("Shift coverage invalid.")
            return False

# Update the schedule with an employee and shift
    def updateSchedule(self, employeeId, shiftId):
        print(f"Schedule updated with employee {employeeId} and shift {shiftId}.")
        return True

# Calculate total scheduled hours
    def getTotalHoursScheduled(self):
        totalHours = self.totalEmployeesPerDay * 8
        print("Total hours:", totalHours)
        return totalHours
