# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 19:42:27 2017

@author: agngr
"""
import random

max = 100
min = 0

questions=int(raw_input("Please enter number of questions:"))
print("You will have %d questions to answer." % questions)
score = 0

for i in range(questions):
    print("Question %d:" % i)
    value = random.randint(min,max)
    answer = int(raw_input("What percentage of ships are blue, if there are %d out of %d are green?" % (value, max)))
    if float(answer) == 100 *(float(max-value)/float(max)):
        score = score + 1
        print("Correct")
    else:
        print("Incorrect, the correct percentage is %3.2f " % (100.0*float(max-value)/float(max)))
        
print("You achieved %d out of %d, which is %3.2f%%" % (score,questions,(100.0*float(score)/float(questions))))