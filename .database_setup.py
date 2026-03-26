
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("schedule.db")

cursor = connection.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    userId INTEGER PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    phoneNumber TEXT,
    email TEXT,
    password TEXT,
    dob TEXT,
    department TEXT,
    employmentStatus TEXT,
    hourlyRate REAL,
    permission TEXT,
    yearlySalary REAL)""")

# SCHEDULE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Schedule (
    scheduleId INTEGER PRIMARY KEY,
    weekStartDate TEXT,
    weekEndDate TEXT,
    scheduleStatus TEXT,
    departmentId INTEGER,
    totalEmployeesPerDay INTEGER)""")

# SHIFT TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Shift (
    shiftId INTEGER PRIMARY KEY,
    shiftDayOfWeek TEXT,
    shiftStartTime INTEGER,
    shiftEndTime INTEGER)""")

# AVAILABILITY TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Availability (
    availabilityId INTEGER PRIMARY KEY,
    userId INTEGER,
    date TEXT,
    startTime INTEGER,
    endTime INTEGER,
    status TEXT)""")

# TIMESHEET TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Timesheet (
    timesheetId INTEGER PRIMARY KEY,
    shiftId INTEGER,
    userId INTEGER,
    totalHoursWorked REAL)""")

# CHECKLIST TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Checklist (
    checklistId INTEGER PRIMARY KEY,
    shiftId INTEGER,
    userId INTEGER,
    taskDescription TEXT,
    taskStatus TEXT,
    timeSpent REAL)""")

# NOTIFICATION TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Notification (
    notificationId INTEGER PRIMARY KEY,
    message TEXT,
    userId INTEGER,
    status TEXT,
    timestamp TEXT)""")

# INCIDENT FORM TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS IncidentForm (
    incidentId INTEGER PRIMARY KEY,
    userId INTEGER,
    date TEXT,
    description TEXT,
    status TEXT)""")

# Save changes
connection.commit()

print("All database tables created successfully")

# Close connection
connection.close()

print("Database connection closed")
