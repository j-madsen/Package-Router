from Data import packageHash
import Distance
from Truck import Truck
from datetime import time, timedelta

def Main():
        # Initializes three truck objects and separates the packages into individual loads
        truck3 = Truck('HUB',[],0,'At the hub.', timedelta(hours=8, minutes=0, seconds= 0))
        truck2 = Truck('HUB',[],0,'At the hub.', timedelta(hours=8, minutes=0, seconds= 0))
        truck1 = Truck('HUB',[],0,'At the hub.', timedelta(hours=9, minutes=5, seconds= 0))
        firstLoad = [4,12,13,14,15,16,17,19,20,21,34,5,37,38,39,40]
        secondLoad = [1,6,23,22,25,29,26,31,32,27,28,35]
        thirdLoad = [30,8,9,36,40,2,10,7,33,24,3,18,11,23]

        # Algorithm that locates the nearest address to the truck's current location. Once the nearest address
        # is located, marks the package as delivered and updates the truck's information accordingly. Also checks
        # if there are other packages at the address and delivers them. Stops delivering once there are no
        # packages remaining on the truck. O(n^2) time complexity, O(1) space complexity.
        def goDeliver(truck):
            while len(truck.getPackageList()) != 0:
                closestMiles = float('inf')
                nearestAdd = ''
                nextPackage = None
                for package in truck.packageList:
                    distance = float(Distance.calculateDistance(truck.getLocation(), package.getAddress()))
                    if distance < closestMiles:
                        closestMiles = distance
                        nearestAdd = package.getAddress()
                        nextPackage = package
                truck.updateTime(timedelta(minutes=closestMiles / 0.3))
                nextPackage.updateDeliveredTime(truck.getTime())
                nextPackage.updateStatus('Delivered at ' + str(truck.getTime()))
                truck.updateMiles(closestMiles)
                truck.updateLocation(nextPackage.getAddress())
                for package in truck.packageList:
                    if nextPackage.getAddress() == package.getAddress() and nextPackage.getID() is not package.getID():
                        package.updateStatus('Delivered at ' + str(truck.getTime()))
                        package.updateDeliveredTime(truck.getTime())
                        truck.packageList.remove(package)
                truck.packageList.remove(nextPackage)

        # Returns the truck to the hub and updates the truck accordingly. O(1) space/time complexity.
        def returnToHub(truck):
            distance = float(Distance.calculateDistance(truck.getLocation(), 'HUB'))
            truck.updateMiles(distance)
            truck.updateLocation('HUB')

    # Following lines delivers the packages.

        truck2.loadPackage(firstLoad)
        goDeliver(truck2)
        returnToHub(truck2)
        truck1.loadPackage(secondLoad)
        goDeliver(truck1)
        truck2.loadPackage(thirdLoad)
        goDeliver(truck2)

        # Console interface for the user. O(1) time/space complexity.

        exit = ""
        while exit != 4:
            userChoice = input(
                        "Make a selection:" "\n"
                        "1. End of day report" "\n"
                        "2. Package lookup" "\n"
                        "3. Package status by time" "\n"
                        "4. Exit" "\n"
                        "Enter a number: ")

            if userChoice == str(1):
                print("Total miles traveled: ")
                print(str(truck1.getMiles() + truck2.getMiles()))
                print("------------" "\n" "Package overview:" "\n" "------------")
                for i in range(1,41):
                    print(packageHash.search(i).getPackageInfo())

            if userChoice == str(2):
                packageChoice = input("Enter a package ID: ")
                print(packageHash.search(int(packageChoice)).getPackageInfo())

            if userChoice == str(3):
                userInput = input("Enter a time in Military time, HH:MM:SS format: ")
                hour = int(userInput[0:2])
                minute = int(userInput[3:5])
                second = int(userInput[6:8])
                time = timedelta(hours = hour, minutes = minute, seconds = second)
                for i in range(1,41):
                    package = packageHash.search(i)
                    if time >= package.getDepartedTime() and time < package.getDeliveredTime():
                        print("Package ID: " + str(package.getID()) + "| Address: " + package.getAddress() + "| Deadline: " + package.getDeadline() + "| City: " + package.getCity() + "| Zip Code: " + package.getZipCode() + "| Weight: " + package.getWeight() + "| Status: " + "En route.")
                    elif time >= package.getDeliveredTime():
                        print(package.getPackageInfo())
                    elif time < package.getDepartedTime():
                        print("Package ID: " + str(package.getID()) + "| Address: " + package.getAddress() + "| Deadline: " + package.getDeadline() + "| City: " + package.getCity() + "| Zip Code: " + package.getZipCode() + "| Weight: " + package.getWeight() + "| Status: " + "At the hub.")
            if userChoice == str(4):
                exit = 4

Main()
