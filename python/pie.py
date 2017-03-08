import matplotlib.pyplot as plt
import numpy as np

haircolours = ['brown','blonde','black','red']
numberofpeople = [5,3,2,4]

figure = plt.figure()

ax = figure.add_subplot(111)
ax.pie(numberofpeople, labels=haircolours, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.show()
