class Notification:
     def __init__(self, notificationId: int,message:str,userId:int,status:str, timestamp: str):
        self.notificationId:int =notificationId
        self.message: str =message
        self.userId:int =userId
        self.status:str =status
        self.timestamp:str =timestamp

# Validate message text
    def validateMessage(self, message):
        if message != "":
            print("Message valid")
            return True
        else:
            print("Message invalid")
            return False
            
# Get employee list
    def getEmployees(self):
        employees = ["Employee1", "Employee2"]
        print("Employees retrieved")
        return employees

#Validate employee selection
    def validateSelection(self):
        employees = self.getEmployees()
        if len(employees) > 0:
            print("Selection valid")
            return True
        else:
            print("Selection invalid")
            return False
            
#Store notification
    def storeNotification(self):
        self.status = "stored"
        print("Notification stored")
        return True

 #Send notification
    def sendNotification(self):
        self.status = "sent"
        print("Notification sent")
        return True
