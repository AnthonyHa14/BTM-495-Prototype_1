class Address:
    def __init__(self, postalCode,streetName, province):
        self.postalCode= postalCode
        self.streetName = streetName
        self.province =province

# Update address
    def updateAddress(self,postalCode,streetName,province):
        self.postalCode = postalCode
        self.streetName = streetName
        self.province = province
        print("Address updated.")
        return True

 # Get full address
    def getFullAddress(self):
        fullAddress = ( self.streetName + ", " +self.province +", " +self.postalCode )
        print(fullAddress)
        return fullAddress

 # Validate postal code
    def validatePostalCode(self):
        if self.postalCode != "":
            print("Postal code valid.")
            return True
        else:
            print("Postal code invalid.")
            return False
