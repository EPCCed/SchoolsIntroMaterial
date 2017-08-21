# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 19:42:27 2017

@author: agngr
"""
import random
from Tkinter import *
import Tkinter
import tkMessageBox
from PIL import Image, ImageTk

class ConfigWindow():
    def __init__(self, parent):
        self.parent = parent
	self.startFrame = Frame(parent)
    	self.startFrame.pack()
    	self.introLabel = Label(self.startFrame,text="Percentages Quiz") 
    	self.introLabel.grid(column=0,row=0,columnspan=2)	  
    	self.questionsLabel = Label(self.startFrame,text="Enter Number of Questions")
    	self.questionsLabel.grid(column=0,row=1,columnspan=1)
    	self.maxLabel = Label(self.startFrame,text="Enter Maximum Number to use")
    	self.maxLabel.grid(column=0,row=2,columnspan=1)
    	self.questionsEntry = Entry(self.startFrame)
    	self.questionsEntry.insert(0,'10')
    	self.questionsEntry.grid(column=1,row=1)
    	self.maxEntry = Entry(self.startFrame) 
    	self.maxEntry.insert(0,'100')
    	self.maxEntry.grid(column=1,row=2)
        self.reset = Button(self.startFrame, text="Reset", command=self.reset)
        self.reset.grid(column=0,row=3)
        self.reset = Button(self.startFrame, text="Begin", command=self.quiz)
        self.reset.grid(column=1,row=3)

    def reset(self):
        self.questionsEntry.delete(0, END)
        self.questionsEntry.insert(0,'10')
        self.maxEntry.delete(0, END)
        self.maxEntry.insert(0,'100')

    def quiz(self):
        self.child = QuizWindow(int(self.questionsEntry.get()),int(self.maxEntry.get()))


class QuizWindow(Tkinter.Toplevel):
    rowLength = 10
    maxValue = 100
    minValue = 0
    questions = 10
    

    def close_windows(self):

        self.destroy()
        

    def __init__(self,questions, maxValue):
        Tkinter.Toplevel.__init__(self)
        self.title("Questions")
        self.questions = questions
        self.currentQuestion = 1
        self.score=0
        self.maxValue = maxValue
        self.redship= ImageTk.PhotoImage(Image.open("redklingon.jpeg").resize((64, 64), Image.ANTIALIAS))
        self.greenship= ImageTk.PhotoImage(Image.open("greenklingon.jpeg").resize((64, 64), Image.ANTIALIAS))
        self.startFrame = Frame(self)
        self.startFrame.pack()
        self.introLabel = Label(self.startFrame,text="Percentages Quiz Question %d" % self.currentQuestion)
        self.introLabel.grid(column=0,row=0,columnspan=10)
        self.currentAnswer =  random.randint(self.minValue,self.maxValue)
        lastrow = self.drawGrid(self.currentAnswer)
        self.questionLabel = Label(self.startFrame, text="What percentrage are red ships?")
        self.questionLabel.grid(column=0,row=lastrow+1, columnspan=3)
        self.answerEntry = Entry(self.startFrame)
        self.answerEntry.grid(column=3,row=lastrow+1, columnspan=3)
        self.submitButton = Button(self.startFrame, text="Submit Answer", command=self.check)
        self.submitButton.grid(column=6,row=lastrow+1, columnspan=4)

    def check(self):
        if int(self.answerEntry.get())==self.currentAnswer:
            self.score = self.score+1
            tkMessageBox.showinfo("Score", "Correct")
        else:
            tkMessageBox.showinfo("Score", "Incorrect, the answer was %d" % self.currentAnswer)
        self.currentQuestion = self.currentQuestion + 1
        if self.currentQuestion > self.questions:
           tkMessageBox.showinfo("Score", "Your Score was %d out of %d" % (self.score,self.questions))
           self.close_windows()
        else:
           self.currentAnswer =  random.randint(self.minValue,self.maxValue)
           self.drawGrid(self.currentAnswer)
           self.introLabel = Label(self.startFrame,text="Percentages Quiz Question %d" % self.currentQuestion)
           self.introLabel.grid(column=0,row=0,columnspan=10)

    def drawGrid(self,red):
        column=0
        row=1
        for i in range(self.maxValue):
            shipLabel=None
            if i<red:
               shipLabel = Label(self.startFrame,image=self.redship) 
            else:
               shipLabel = Label(self.startFrame, image=self.greenship)
            shipLabel.grid(column=column, row=row)
            column = column+1
            if column >= self.rowLength:
               column=0
               row = row+1
        return row               
"""                
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

"""
def main():
    root = Tk()
    configwindow = ConfigWindow(root) 
    root.mainloop()      

if __name__=="__main__":
    main()
