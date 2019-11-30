listTest = []

while True:
    inputDecision = input("1:enque 2:deque")
    length = len(listTest)
    if(inputDecision == "1"):
        if(length == 10):
            print("You can't input any more integers OverFlow Err")
        else:
            inputNumber = input("type number to enter")
            listTest.append(inputNumber)
            print(listTest)

    elif(inputDecision == "2"):
        if(length == 0):
            print("You can't deque any more integers UnderFlow Err")
        else:
            listTest.pop(0)
            print(listTest)