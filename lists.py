testList = [5,3,24,20,7,1,12]

#Function to find max and min of given list value
"""
def minMax(testList):
    y = testList[0]
    for i in range(len(testList)):
        if(y < testList[i]):
            y = testList[i]

    x = testList[0]
    for j in range(len(testList)):
        if(x > testList[j]):
            x = testList[j]

    print(y,x)
        
minMax(testList)"""

"""
#Reverses the List
def reverseList(testList):
    newList = []
    for i in range(len(testList)):
        newList.append(testList[(len(testList)-1)-i])

    print(newList)

reverseList(testList)

#Only odd Numbers
def oddNumbers(testList):
    oddList = []
    for i in range(len(testList)):
        if((testList[i] % 2) != 0):
            oddList.append(testList[i])

    print(oddList)

oddNumbers(testList)"""

def listCreator():
    userInput = True
    dataList = []
    while userInput == True:
        userNumber = input("type a number")
        if(userNumber == "No"):
            userInput = False
        else:
            dataList.append(int(userNumber))
    minMaxFromUser(dataList)
        
def minMaxFromUser(testList):
    y = testList[0]
    for i in range(len(testList)):
        if(y < testList[i]):
            y = testList[i]

    x = testList[0]
    for j in range(len(testList)):
        if(x > testList[j]):
            x = testList[j]

    print(y,x)
        
listCreator()
