import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Hidden Stuff you can't see
graphList = []
def numberMaker():
    for i in range(10):
        randomNumber = random.randint(0,10)
        graphList.append(randomNumber)
    return graphList

#The function you can't see being called
numberMaker()

#A system of both plotting and 
print(graphList)
plt.plot(graphList)
plt.ylabel('some numbers')
plt.show()