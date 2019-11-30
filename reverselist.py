theList = [1,2,3,4,5]
newList = []

for i in range(len(theList)):
    appender = len(theList) - i
    newList.append(appender)

print(newList)