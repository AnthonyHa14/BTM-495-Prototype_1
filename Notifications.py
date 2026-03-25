class Notification:
    def __init__(self,notificationId,message, userId, createdDateTime,status):
        self.notificationId =notificationId
        self.message =message
        self.userId =userId
        self.createdDateTime =createdDateTime
        self.status = status


# Validate message text
    def validateMessage(self, message):
        if message != "":
            print("Message valid.")
            return True
        else:
            print("Message invalid.")
            return False
            
# Get employee list
    def getEmployees(self):
        employees = ["Employee1", "Employee2"]
        print("Employees retrieved.")
        return employees

#Validate employee selection
    def validateSelection(self):
        employees = self.getEmployees()
        if len(employees) > 0:
            print("Selection valid.")
            return True
        else:
            print("Selection invalid.")
            return False
            
#Store notification
    def storeNotification(self):
        self.status = "stored"
        print("Notification stored.")
        return True

 #Send notification
    def sendNotification(self):
        self.status = "sent"
        print("Notification sent.")
        return True
