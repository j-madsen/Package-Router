from Data import distanceList, addDict

# Calculates the distance between two addresses. O(1) time/space complexity.
def calculateDistance(add1,add2):
    try:
        return distanceList[addDict[add1]][addDict[add2]]
    except IndexError:
        return distanceList[addDict[add2]][addDict[add1]]

