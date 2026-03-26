class User:
    def __init__(self, userId: int, firstName: str, lastName: str,phoneNumber: str,email: str,password: str,dob: str):
        self.userId:int =userId
        self.firstName:str =firstName
        self.lastName: str=lastName
        self.phoneNumber:str =phoneNumber
        self.email:str =email
        self.password:str =password
        self.dob:str =dob
        self.address =None

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
        
# Validate the fields of the form
def submitForValidation(self):

    # Check fields are not empty
    if (self.firstName == "" or
        self.lastName == "" or
        self.email == "" or
        self.password == ""):
        print("Validation failed: Missing required fields.")
        return False
            
    # Simple email format check
    if "@" not in self.email or "." not in self.email:
        print("Validation failed: Invalid email format.")
        return False

    # Simple password length check
    if len(self.password) < 6:
        print("Validation failed: Password too short")
        return False
    print("Validation successful")
    return True
            
 # Login using email and password
    def login(self, email,password):
        if self.email == email and self.password == password:
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False

# Logout the user
    def logout(self):
        print("User logged out")
        return True

# Update phone number and email
    def updateProfile(self,phoneNumber, email):
        self.phoneNumber = phoneNumber
        self.email = email
        print("Profile updated")
        return True

 # Submit an incident form
    def submitIncidentForm(self,description):
        from Incident_Form import IncidentForm
        form = IncidentForm(1,self.userId,"2026-03-25" ,description, "submitted")
        print("Incident form submitted")
        return form

# Select the incident form tab
    def selectIncidentFormTab(self):
        print("Incident Form tab selected.")
        return "Incident Form tab selected"
