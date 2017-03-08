import matplotlib.pyplot as plt
import numpy as np
import csv


datafile = open('hairs.csv')
csvReader = csv.reader(datafile)
headers = csvReader.next()
datalines = []
for row in csvReader:
    datalines.append(row)


figure = plt.figure()

ax = figure.add_subplot(111)
ax.pie(datalines[0], labels=headers, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.show()
