#Reverse The Word
"""
word = input("type any word: ")
count = len(word) - 1

def recursiveTheWord(number, newList):
    if(number < 0):
        finalOutput = ''.join(newList)
        print(finalOutput)
        exit()
    newList.append(word[number])
    number -= 1
    recursiveTheWord(number, newList)

recursiveTheWord(count, [])
"""

#Find Factorial Number
"""
number = int(input("type any number: "))
count = number - 1

def factorialNumber(numberX, countX):
    if(countX == 0):
        print(numberX)
        exit()
    numberX *= countX
    countX -= 1
    factorialNumber(numberX, countX)
factorialNumber(number, count)
"""


listy = [1,2,3,4,5,6,7,8,9,10]
listLen = len(listy)
inputNumber = 7
count = 0

def binarySearch(listLenX, listLen, listx):
    if(listx[count] == inputNumber):
        print(listx[count])
        
    if(inputNumber > (listLenX/2)):
        listLenX = round(listLenX/4 + listLenX/2)
        print(listLenX)
        binarySearch(listLenX, listLen, listx)
        
    elif(inputNumber < (listLenX/2)):
        listLenX = round(listLenX/2 - listLenX/4)
        print(listLenX)
        binarySearch(listLenX, listLen, listx)

binarySearch(listLen, listLen, listy)






