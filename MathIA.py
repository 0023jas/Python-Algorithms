import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
numberList = []
for i in range(100):
    number = 26 ** i
    number = 1/number
    numberList.append(number)

print(numberList)

plt.plot(numberList)
plt.title('Decryption Chance by Length of Key')
plt.ylabel('Decryption Chance')
plt.xlabel('Length of Key')
plt.show()