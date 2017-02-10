# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 19:42:27 2017

@author: agngr
"""
import random



questions=int(raw_input("Please enter number of questions:"))
print("You will have %d questions to answer." % questions)
max = int(raw_input("Please enter a highest number to test with:"))
min = 0
score = 0

for i in range(questions):
    print("Question %d:" % i)
    value = random.randint(min,max)
    answer = int(raw_input("What percentage of ships are blue, if there are %d out of %d are green?" % (value, max)))
    if float(answer) == round(100 *(float(max-value)/float(max))):
        score = score + 1
        print("Correct")
    else:
        print("Incorrect, the correct percentage is %3.2f " % round(100.0*float(max-value)/float(max)))
        
print("You achieved %d out of %d, which is %3.2f%%" % (score,questions,(100.0*float(score)/float(questions))))
