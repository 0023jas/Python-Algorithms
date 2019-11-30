import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.plot([5.28, 8.26, 14.68, 33.02, 132.17], [53.7, 39.3, 26.0, 13.9, 5.47], 'ro')
plt.ylabel('some numbers')
plt.show()