class Manager(User):
    def __init__(self, userId,firstName, lastName, phoneNumber,email, password,dob, permission,yearlySalary):
        super().__init__(userId, firstName,lastName, phoneNumber,email, password,dob)
        self.permission= permission
        self.yearlySalary =yearlySalary
