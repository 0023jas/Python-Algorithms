import random
from random import shuffle
import time

sudokuPuzzle = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
runCounter = 0
checkTestedBefore = 0

for i in range(len(sudokuPuzzle)):
    if(i == 0):
        for x in range(1,10):
            sudokuPuzzle[i].append(x)
    else:
        for x in range(9):
            sudokuPuzzle[i].append(0)
shuffle(sudokuPuzzle[0])
print(sudokuPuzzle)

sudokuPuzzleCheck = False
while sudokuPuzzleCheck == False:
    runCounter = runCounter + 1
    sudokuPuzzleComplete = False
    count = 1
    while sudokuPuzzleComplete == False:
        possiblePostions1 = [0,1,2]
        possiblePostions2 = [3,4,5]
        possiblePostions3 = [6,7,8]
        for i in range(1,10):
            #print(i)
            numberPosition = sudokuPuzzle[count-1].index(i)
            #print(numberPosition)
            if(numberPosition < 3):
                randomListInteger = random.choice(possiblePostions2)
                possiblePostions2.remove(randomListInteger)
                sudokuPuzzle[count][randomListInteger] = i
            elif(numberPosition < 6):
                randomListInteger = random.choice(possiblePostions3)
                possiblePostions3.remove(randomListInteger)
                sudokuPuzzle[count][randomListInteger] = i
            elif(numberPosition < 9):
                randomListInteger = random.choice(possiblePostions1)
                possiblePostions1.remove(randomListInteger)
                sudokuPuzzle[count][randomListInteger] = i
        if(count < 9):
            count = count + 1
        if(count == 9):
            sudokuPuzzleComplete = True
    correctLineCounter = 0
    for k in range(len(sudokuPuzzle)):
        lineCount = 0
        verticalList = []
        for l in range(len(sudokuPuzzle)):
            #lineCount = lineCount + sudokuPuzzle[l][k].count(l)
            verticalList.append(sudokuPuzzle[l][k])
        for a in range(9):
            lineCount = lineCount + verticalList.count(a)
        if(lineCount == 9):
            correctLineCounter = correctLineCounter + 1
            #print(correctLineCounter)
        #print(correctLineCounter)
    if(correctLineCounter == 9):
        sudokuPuzzleCheck = True
        print("this Worked")
        print(sudokuPuzzle)
        time.sleep(100000)
    else:
        print(sudokuPuzzle)
        print(runCounter)
        #checkTestedBefore = 2
        """
        y = 2
        for y in range(7):
            sudokuPuzzle[y+2].clear
        #print("this didn't work")
        #print(correctLineCounter)
        #if(correctLineCounter > 2):
            #time.sleep(0.5)
        print(sudokuPuzzle)"""

        

    



#create first row, then specifically place the numbers based on where the same number is in a different row
#take 1 as the first integer
#find the position of the ones in all the higher positions
#create list of positions where 1 can't go
#create list of positions where 1 can go
#create list of positions where 1 has to go 
#based of the last two lists randomize the position of 1 within the list
# trying doing it list by list first before fully automating
