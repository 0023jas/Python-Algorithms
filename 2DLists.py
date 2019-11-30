import random 
"""
marksForEachStudent = [[6, 4, 5],[4, 7, 6],[3, 2, 3],[9,9,9]]
classGradeList = []
classAverage = 0
for i in range(len(marksForEachStudent)):
    for j in range(len(marksForEachStudent[i])):
        classGradeList.append(marksForEachStudent[i][j])

print(classGradeList)
for k in range(len(classGradeList)):
    classAverage = classGradeList[k] + classAverage

classAverage = classAverage/k
print(classAverage)

studentGradeList = []
studentAverageList = []

for l in range(len(marksForEachStudent)):
    accumulator = 0
    studentGradeList = []
    for m in range(len(marksForEachStudent[l])):
        studentGradeList.append(marksForEachStudent[l][m])
    
    for n in range(len(studentGradeList)):
        accumulator += studentGradeList[n]
    
    accumulator = accumulator/(n+1)
    studentAverageList.append(accumulator)

print(studentAverageList)
"""
matrix1 = []
matrix2 = []
matrixAdder1 = []
matrixAdder2 = []
for i in range(3):
    matrixAdder1 = []
    matrixAdder2 = []
    for j in range(3):
        randomInt = random.randint(0,10)
        matrixAdder1.append(randomInt)
    matrix1.append(matrixAdder1)

    for k in range(3):
        randomInt = random.randint(0,10)
        matrixAdder2.append(randomInt)
    matrix2.append(matrixAdder2)

print(matrix1)
print(matrix2)

if(len(matrix1) == len(matrix2)):
    print("rows is equivalent")
