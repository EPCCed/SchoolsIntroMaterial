import matplotlib.pyplot as plt
import numpy as np
import csv
import math

datafile = open('hairs2.csv')
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

charts = len(datalines)
maxperrow = min(3, charts)
rows =int(math.ceil(float(charts)/float(maxperrow)))
for x in xrange(charts):
    ax = figure.add_subplot(rows, maxperrow, x+1)

    ax.bar(y_positions, datalines[x], color='r')

    ax.set_xticks(y_positions)
    ax.set_xticklabels(headers, rotation=90)

    ax.set_xlabel('Hair Colours')
    ax.set_title('Hair Colours\n Class %d' % x)

plt.savefig('foo.png')
plt.show()
