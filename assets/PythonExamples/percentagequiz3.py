# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 19:42:27 2017

@author: agngr
"""
import random

def askquestion(number,min,max):
    value = random.randint(min,max)
    print("Question %d:" % number )
    answer = int(raw_input("What percentage of ships are blue, if there are %d out of %d are green?" % (value, max)))
    if float(answer) == round(100 *(float(max-value)/float(max))):
        print("Correct")
        return 1
    else:
        print("Incorrect, the correct percentage is %3.2f " % round(100.0*float(max-value)/float(max)))
        return 0

def get_questions_setup():
    questions=int(raw_input("Please enter number of questions:"))
    max = int(raw_input("Please enter a highest number to test with:"))
    min = 0
    return (questions,min,max)

def run_quiz():
    score = 0
    questions,min,max = get_questions_setup()
    print("You will have %d questions to answer." % questions)
    for i in range(questions):
        score = score + askquestion(i,min,max)    
    print("You achieved %d out of %d, which is %3.2f%%" % (score,questions,(100.0*float(score)/float(questions))))


if __name__=="__main__":
    run_quiz()
