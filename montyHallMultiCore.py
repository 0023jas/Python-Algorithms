#1. random generate three doors
#2. Set one door to be the correct answer
#3. Select a door that isn't the correct and remove it
#4. Change the answer and see if it is correct
import random
import time
from multiprocessing import Process
import multiprocessing as mp
import sys


cpu_count = mp.cpu_count()

arguments = {
'-c' : 0,
'-n' : 0,
'-t' : 0
}

for x in sys.argv:
	if x in arguments.keys():
		arguments[x] = 1

count = 100000

def multi_start():
	for x in range(int(count / cpu_count)):
		wins_loss = createDoors()
	

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
        return True
    elif(doors[doorSelect] == 0):
        return False

if arguments['-n'] == 1:
	wins = 0
	losses = 0
	start = time.time()
	for i in range(100000):
	     result = createDoors()
	     if result:
                 wins += 1
	     elif not(result):
	         losses += 1
	end = time.time()
	print(end-start)
	print("%d/%d"%(wins,losses))
if arguments['-c'] == 1:
	start = time.time()
	multi = []
	alive = 0
	for x in range(cpu_count):
		multi.append(Process(target = multi_start))
	for x in multi:
		x.start()
	while alive != 5:
		for x in range(len(multi)):
			if multi[x].is_alive():
				multi[x].join()
				multi.pop(x)
				alive += 1 
				break
	end = time.time()
	print(end-start)
