import matplotlib.pyplot as plt
import numpy as np
import csv


datafile = open('hairs.csv')
csvReader = csv.reader(datafile)
headers = csvReader.next()
datalines = []
for row in csvReader:
    datalines.append(row)


#haircolours = ['brown','blonde','black','red']
#numberofpeople = [5,3,2,4]

#y_positions = np.arange(len(haircolours))
y_positions = np.arange(len(headers))

figure = plt.figure()

ax = figure.add_subplot(111)

#ax.bar(y_positions, numberofpeople, color='r')
ax.bar(y_positions, datalines[0], color='r')

ax.set_xticks(y_positions)
#ax.set_xticklabels(haircolours)
ax.set_xticklabels(headers)

ax.set_xlabel('Hair Colours')
ax.set_title('People with Hair Colours')

plt.savefig('foo.png')
plt.show()
