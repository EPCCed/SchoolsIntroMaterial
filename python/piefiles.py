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


figure = plt.figure()

charts = len(datalines)
maxperrow = min(3, charts)
rows =int(math.ceil(float(charts)/float(maxperrow)))
for x in xrange(charts):
    ax = figure.add_subplot(rows,maxperrow,x+1)
    ax.pie(datalines[x], labels=headers, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    ax.set_title('Hair Colours\n Class %d' % x)
plt.savefig('foo.png')
plt.show()
