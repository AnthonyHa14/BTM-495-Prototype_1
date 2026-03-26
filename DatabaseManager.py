class DatabaseManager:
    def __init__(self, connectionString):
        self.connectionString = connectionString
        self.isConnected = False

#Connect to the database
    def connect(self):
        self.isConnected = True
        print("Database successfully connected")
        return True
      
#Disconnect from the database
    def disconnect(self):
        self.isConnected = False
        print("Database disconnected")
        return True

  #Execute a database query
    def executeQuery(self, query):
        if not self.isConnected:
            print("Database not connected")
            return False
        if query == "":
            print("Empty query")
            return False
        print("Query executed:", query)
        return True
      
   #Save an entity in the database
    def saveEntity(self, entity):
        if self.isConnected:
            print("Entity saved")
            return True
        print("Save failed")
        return False

  #Save a user account in the database
    def saveUserAccount(self, userData):
        if self.isConnected:
            print("User account saved")
            return True
        print("User account save failed")
        return False

  #Assign a primary key to an entity
    def assignPrimaryKey(self, entity):
        if hasattr(entity, "userId"):
            print("Primary key assigned:", entity.userId)
            return entity.userId
        print("Default primary key assigned: 1")
        return 1

    #Get the employees from the database
    def getEmployees(self):
        if self.isConnected:
            employees = ["Employee1", "Employee2"]
            print("Employees retrieved")
            return employees
        print("No employees retrieved")
        return []

  #Show a success confirmation message
    def successConfirmation(self):
        message = "Action completed successfully"
        print(message)
        return message

#Flag a task
    def flagTask(self, taskId):
        message = f"Task {taskId} flagged"
        print(message)
        return message
