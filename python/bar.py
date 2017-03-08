import matplotlib.pyplot as plt
import numpy as np

haircolours = ['brown','blonde','black','red']
numberofpeople = [5,3,2,4]

y_positions = np.arange(len(haircolours))

figure = plt.figure()

ax = figure.add_subplot(111)

ax.bar(y_positions, numberofpeople, color='r')
ax.set_xticks(y_positions)
ax.set_xticklabels(haircolours)
ax.set_xlabel('Hair Colours')
ax.set_title('People with Hair Colours')

plt.show()
