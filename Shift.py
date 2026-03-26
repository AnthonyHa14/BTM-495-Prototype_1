class Shift:
    def __init__(self, scheduleId: int,weekStartDate: str,weekEndDate:str,scheduleStatus:str,departmentId:int,totalEmployeesPerDay: int):
        self.scheduleId:int =scheduleId
        self.weekStartDate: str= weekStartDate
        self.weekEndDate: str =weekEndDate
        self.scheduleStatus:str = scheduleStatus
        self.departmentId:int =departmentId
        self.totalEmployeesPerDay:int =totalEmployeesPerDay

# Create a new shift
    def createShift(self):
        print("Shift successfully created")
        return True

# Update shift start and end times
    def updateShiftTimes(self, startTime, endTime):
        self.shiftStartTime = startTime
        self.shiftEndTime = endTime
        print("Shift times successfully updated")
        return True

# Calculate the shift duration
    def getShiftDuration(self):
        duration = self.shiftEndTime - self.shiftStartTime
        print("Shift duration:", duration)
        return duration
