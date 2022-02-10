from Data import packageHash

# Truck class houses methods to work with truck objects.

class Truck:
    def __init__(self, location, packageList, miles, status, time):
        self.location = location
        self.packageList = packageList
        self.miles = miles
        self.status = status
        self.time = time

    # Getters to get values of truck attributes. O(1) space/time complexity.
    def getLocation(self):
        return self.location
    def getPackageList(self):
        return self.packageList
    def getMiles(self):
        return self.miles
    def getStatus(self):
        return self.status
    def getTime(self):
        return self.time

    # Setters to update package attributes. O(1) space/time complexity.
    def updateLocation(self,location):
        self.location = location
    def updatePackageList(self, package):
        self.packageList.append(package)
    def updateStatus(self, status):
        self.status = status
    def updateMiles(self, miles):
        self.miles += miles
    def updateTime(self, time):
        self.time += time

    # Loads the truck with packages and marks the departure time. O(N) time O(1) space.
    def loadPackage(self,load):
        for id in load:
            self.packageList.append(packageHash.search(id))
            packageHash.search(id).updateDepartedTime(self.getTime())
            packageHash.search(id).updateStatus('En route.')


