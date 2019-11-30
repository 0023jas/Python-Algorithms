#1. random generate three doors
#2. Set one door to be the correct answer
#3. Select a door that isn't the correct and remove it
#4. Change the answer and see if it is correct
import random
import time
start = time.time()

wins = []
losses = []

def createDoors():
    doors = [0,0,0]
    doorCreate = random.randint(0,2)
    doors[doorCreate] = 1 

    doorSelect = random.randint(0,2)
    if(doors[doorSelect] == 1):
        if(doorSelect == 2):
            doorSelect = doorSelect-1
            doors.pop(1)

        elif(doorSelect == 1):
            doorSelect = doorSelect-1
            doors.pop(0)

        elif(doorSelect == 0):
            doors.pop(2)

    elif(doors[doorSelect] == 0):
        if(doorSelect == 2):
            doorSelect = doorSelect-1
            if(doors[1] == 0):
                doors.pop(1)
            elif(doors[0] == 0):
                doors.pop(0)
        elif(doorSelect == 1):
            if(doors[2] == 0):
                doors.pop(2)
            elif(doors[0] == 0):
                doorSelect = doorSelect-1
                doors.pop(0)
        elif(doorSelect == 0):
            if(doors[1] == 0):
                doors.pop(1)
            elif(doors[2] == 0):
                doors.pop(2)

    if(doorSelect == 0):
        doorSelect = 1
    elif(doorSelect == 1):
        doorSelect = 0

    if(doors[doorSelect] == 1):
        wins.append(1)
    elif(doors[doorSelect] == 0):
        losses.append(0)

for i in range(100000):
    createDoors()

totalWins = len(wins)
totalLosses = len(losses)

print(totalWins)
print(totalLosses)

end = time.time()
runTime = (end-start)
print(runTime)
