class Shift:
    def __init__(self, shiftId, shiftDayOfWeek,shiftStartTime,shiftEndTime):
        self.shiftId = shiftId
        self.shiftDayOfWeek =shiftDayOfWeek
        self.shiftStartTime =shiftStartTime
        self.shiftEndTime =shiftEndTime


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
