listTest = []

while True:
    inputDecision = input("1:Push 2:Pop")
    if(inputDecision == "1"):
        length = len(listTest)
        if(length == 10):
            print("You can't input any more integers OverFlow Err")
        else:
            inputNumber = input("type number to enter")
            listTest.append(inputNumber)
            print(listTest)

    elif(inputDecision == "2"):
        length = len(listTest)
        if(length == 0):
            print("You can't pop any more integers UnderFlow Err")
        else:
            listTest.pop(length-1)
            print(listTest)