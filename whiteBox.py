import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Three lists of three different data types
letters = ['a','b','c','d']
numsLetters = [1,'2','a',5]
nums = [1,2,3,4]

#Testing if they work
print(letters)
plt.plot(letters)
plt.ylabel('some letters')
plt.show()

#Testing if they work
print(numsLetters)
plt.plot(numsLetters)
plt.ylabel('some letters n numbers')
plt.show()

#Testing if they work
print(nums)
plt.plot(nums)
plt.ylabel('some numbers')
plt.show()