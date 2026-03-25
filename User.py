class User:
    def __init__(self, userId,firstName, lastName,phoneNumber,email,password,dob):
        self.userId = userId
        self.firstName= firstName
        self.lastName= lastName
        self.phoneNumber= phoneNumber
        self.email =email
        self.password =password
        self.dob =dob
        self.address = None

# Fill out the registration form with the given info
    def fillOutForm(self, firstName, lastName,phoneNumber, password,dob, address):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.password = password
        self.dob = dob
        self.address = address
        print("Form filled successfully.")
        return True
        
# Validate the required fields
    def submitForValidation(self):
        if (self.firstName != "" and
            self.lastName != "" and
            self.email != "" and
            self.password != ""):
            print("Validation successful.")
            return True
        else:
            print("Validation failed.")
            return False
            
 # Login using email and password
    def login(self, email,password):
        if self.email == email and self.password == password:
            print("Login successful.")
            return True
        else:
            print("Login failed.")
            return False

# Logout the user
    def logout(self):
        print("User logged out.")
        return True

# Update phone number and email
    def updateProfile(self,phoneNumber, email):
        self.phoneNumber = phoneNumber
        self.email = email
        print("Profile updated.")
        return True

 # Submit an incident form
    def submitIncidentForm(self,description):
        from Incident_Form import IncidentForm
        form = IncidentForm(1,self.userId,"2026-03-25" ,description, "submitted")
        print("Incident form submitted.")
        return form

# Select the incident form tab
    def selectIncidentFormTab(self):
        print("Incident Form tab selected.")
        return "Incident Form tab selected"
