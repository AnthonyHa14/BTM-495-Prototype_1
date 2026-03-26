class IncidentForm:
    def __init__(self, incidentId: int,userId: int,date: str,description: str, status: str):
        self.incidentId: int =incidentId
        self.userId: int= userId
        self.date: str= date
        self.description:str = description
        self.status: st =status

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
