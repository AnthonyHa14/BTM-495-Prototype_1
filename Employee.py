class Employee(User):
    def __init__(self, userId, firstName, lastName, phoneNumber, email, password,dob, department, employmentStatus, hourlyRate):
        super().__init__(userId, firstName,lastName, phoneNumber, email,password, dob)
        self.department =department
        self.employmentStatus= employmentStatus
        self.hourlyRate =hourlyRate
