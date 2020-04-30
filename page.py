#import module from tkinter for UI
from tkinter import *
import os, sys
import cv2
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("python3 face_datasets.py")
    
def function2():
    
    os.system("python3 training.py")

def function3():

    os.system("python3 face_recognition2.py")

def function5():    
   os.system("python3 face_recognition3.py")
   
def function6():

    root.destroy()

def function7():
    os.system("python3 contactHR.py")
    
#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Add Face (For New Employees)",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Confirm New User",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Check In",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Check Out",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Contact HR",font=('times new roman',20),bg="#0D47A1",fg="white",command=function7).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
