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



class Address:
    def __init__(self, postalCode,streetName, province):
        self.postalCode= postalCode
        self.streetName = streetName
        self.province =province


class IncidentForm:
    def __init__(self, incidentId,userId, date,description, status):
        self.incidentId =incidentId
        self.userId =userId
        self.date =date
        self.description =description
        self.status =status

class Notification:
    def __init__(self,notificationId,message, userId, createdDateTime,status):
        self.notificationId =notificationId
        self.message =message
        self.userId =userId
        self.createdDateTime =createdDateTime
        self.status = status

class Schedule:
    def __init__(self, scheduleId,weekStartDate, weekEndDate, scheduleStatus,departmentId,totalEmployeesPerDay):
        self.scheduleId =scheduleId
        self.weekStartDate= weekStartDate
        self.weekEndDate =weekEndDate
        self.scheduleStatus= scheduleStatus
        self.departmentId =departmentId
        self.totalEmployeesPerDay =totalEmployeesPerDay
