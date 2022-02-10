import csv
from Package import Package
import hashTable

# Reads package information from the CSV file and creates package objects to insert into the hash table.
# O(N) time complexity O(N) space complexity.
file = open('Package.csv', 'r')
reader = csv.reader(file)
packageHash = hashTable.ChainingHashTable()
for pkg in reader:
    newPackage = Package(int(pkg[0]), pkg[1], pkg[5], pkg[2], pkg[4], pkg[6], "At the hub.", None, None)
    packageHash.insert(newPackage.getID(), newPackage)



# Reads distances from distance CSV and adds them to the list of distances. O(N) time complexity/ O(N) space..
distanceList = []
file = open('distance.csv', 'r')
reader = csv.reader(file, delimiter=",")
for row in reader:
    distanceList.append(row)

# Reads addresses from address CSV and adds them to the dictionary of addresses. O(N) time complexity/ O(N) space.
addDict = {}
file = open('address.csv', 'r')
reader2 = csv.reader(file)
i = 0
for row in reader2:
    addDict[''.join(row)] = i
    i+=1
