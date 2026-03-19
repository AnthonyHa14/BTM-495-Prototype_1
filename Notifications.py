class Notification:
    def __init__(self,notificationId,message, userId, createdDateTime,status):
        self.notificationId =notificationId
        self.message =message
        self.userId =userId
        self.createdDateTime =createdDateTime
        self.status = status
