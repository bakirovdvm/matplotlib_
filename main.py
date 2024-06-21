import matplotlib.pyplot as plt
import numpy as np

'''
Matplotlib
https://matplotlib.org/stable/gallery/index
'''

width = 0.4
x_list = list(range(0, 5))
y1_list = [22, 17, 81, 41, 25]
y2_list = [62, 37, 39, 36, 49]


plt.figure()
plt.subplot(2, 2, 1)

plt.title('Salary graph')
plt.xlabel('label')
plt.ylabel('salary, $')
plt.plot(x_list, y1_list, label='Mark', marker='o')
plt.plot(x_list, y2_list, label='Steben', marker='^')
plt.legend()


a_indexes = np.arange(len(x_list))


plt.subplot(2, 2, 2)
plt.title('A and B lists')
plt.xticks(a_indexes, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
plt.xlabel('days')
plt.ylabel('salary, $')
plt.bar(a_indexes - (width/2), y1_list, label='Mark', width=width)
plt.bar(a_indexes + (width/2), y2_list, label='Steben', width=width)
plt.legend()


plt.subplot(2, 1, 2)
plt.title('Another graph')
plt.xticks(a_indexes, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
plt.xlabel('days')
plt.ylabel('salary, $')
plt.bar(a_indexes - (width/2), y1_list, label='Mark', width=width)
plt.bar(a_indexes + (width/2), y2_list, label='Steben', width=width)
plt.legend()

plt.show()