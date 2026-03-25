class IncidentForm:
    def __init__(self, incidentId,userId, date,description, status):
        self.incidentId =incidentId
        self.userId =userId
        self.date =date
        self.description =description
        self.status =status

 # Validate incident form
    def validateIncidentForm(self):
        if self.description != "":
            print("Incident form valid.")
            return True
        else:
            print("Incident form invalid.")
            return False

  #Submit incident form
    def submitIncidentForm(self):
        if self.validateIncidentForm():
            self.status = "submitted"
            print("Incident form submitted.")
            return True
        return False
        
 #View incident details
    def viewIncidentForm(self):
        details = ( f"Incident {self.incidentId}: " f"{self.description}" )
        print(details)
        return details
