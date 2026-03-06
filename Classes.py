class User:
    def __init__(self, userId,firstName, lastName,phoneNumber,email,password,dob):
        self.userId = userId
        self.firstName= firstName
        self.lastName= lastName
        self.phoneNumber= phoneNumber
        self.email =email
        self.password =password
        self.dob =dob


class Employee(User):
    def __init__(self, userId, firstName, lastName, phoneNumber, email, password,dob, department, employmentStatus, hourlyRate):
        super().__init__(userId, firstName,lastName, phoneNumber, email,password, dob)
        self.department =department
        self.employmentStatus= employmentStatus
        self.hourlyRate =hourlyRate


class Manager(User):
    def __init__(self, userId,firstName, lastName, phoneNumber,email, password,dob, permission,yearlySalary):
        super().__init__(userId, firstName,lastName, phoneNumber,email, password,dob)
        self.permission= permission
        self.yearlySalary =yearlySalary
