class Task:
    def __init__(self, taskId, taskName,taskDescription, status,timeSpent, assignedDate):
        self.taskId= taskId
        self.taskName =taskName
        self.taskDescription =taskDescription
        self.status =status
        self.timeSpent= timeSpent
        self.assignedDate= assignedDate

 # Create a new task
    def createTask(self, taskName, taskDescription):
        task = {"taskName": taskName,"taskDescription": taskDescription,"status": "open"}
        print("Task created:", task)
        return task

#Update the task description
    def updateTask(self, taskName, taskDescription):
        self.taskDescription = taskDescription
        print("Task successfully updated")
        return True

#View the checklist
    def viewChecklist(self):
        checklist = [self]
        print("Checklist viewed")
        return checklist

# Mark a task as complete
    def markTaskComplete(self, taskId, status):
        self.taskStatus = status
        print(f"Task {taskId} marked as {status}")
        return True

 #Save the checklist
    def saveChecklist(self):
        print("Checklist successfully saved")
        return True

# Flag a task with no response
    def flagNoResponse(self, taskId):
        message = f"Task {taskId} flagged"
        print(message)
        return message

#Get the checklist assignment list
    def getChecklistAssignmentList(self):
        assignmentList = [self.checklistId]
        print("Checklist assignment list:", assignmentList)
        return assignmentList
        
#Validate the response to a task
    def validateResponse(self, taskId):
        if self.taskStatus != "":
            print("Response confirmed")
            return True
        else:
            print("Response is invalid.")
            return False

# Send a reminder notification
    def reminderNotification(self):
        message = "Reminder sent"
        print(message)
        return message
