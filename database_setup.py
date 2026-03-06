class DatabaseManager:

    def __init__(self, db_name="schedule.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Users (userId INTEGER PRIMARY KEY, firstName TEXT, lastName TEXT, email TEXT)"
        )

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Schedule (scheduleId INTEGER PRIMARY KEY, weekStartDate TEXT, weekEndDate TEXT, scheduleStatus TEXT)"
        )

        self.connection.commit()

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    db = DatabaseManager()
    db.create_tables()
    db.close()
