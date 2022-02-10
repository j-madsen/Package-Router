import Data

# Package class houses methods to work with package objects.

class Package:
    def __init__(self, packageID, address, deadline, city, zipCode, weight, status, departedHub, delivered):
        self.packageID = packageID
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zipCode = zipCode
        self.weight = weight
        self.status = status
        self.departedHub = departedHub
        self.delivered = delivered

    # Getters to get values of package attributes. O(1) space/time complexity.
    def getID(self):
        return self.packageID
    def getAddress(self):
        return self.address
    def getDeadline(self):
        return self.deadline
    def getCity(self):
        return self.city
    def getZipCode(self):
        return self.zipCode
    def getWeight(self):
        return self.weight
    def getStatus(self):
        return self.status
    def getDepartedTime(self):
        return self.departedHub
    def getDeliveredTime(self):
        return self.delivered
    def getStatus(self):
        return self.status
    def getPackageInfo(self):
        return "Package ID: " + str(self.packageID) + "| Address: " + self.address + "| Deadline: " + self.deadline + "| City: " + self.city + "| Zip Code: " + self.zipCode + "| Weight: " + self.weight + "| Status: " + self.status
    def getPackages(self, id):
        selectedPackage = Data.packageHash.search(id)
        return selectedPackage

    # Setters to update package attributes. O(1) space/time complexity.
    def updateStatus(self, status):
        self.status = status
    def updateDepartedTime(self,time):
        self.departedHub = time
    def updateDeliveredTime(self,time):
        self.delivered = time

