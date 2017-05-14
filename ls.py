#!/usr/bin/env python3
import tkinter
from tkinter import messagebox
from tkinter import*

import os

def f1():
	os.system("ls>new.txt")
	x=open("new.txt","r")
	tkinter.messagebox.showinfo("ALL FILES    ",x.read())
def f2():
	os.system("date>new.txt")
	x=open("new.txt","r")
	tkinter.messagebox.showinfo("Date    ",x.read())
def f3():
	os.system("cal>new.txt")
	x=open("new.txt","r")
	tkinter.messagebox.showinfo("CALENDER   ",x.read())
def f4():
	os.system("ps>new.txt")
	x=open("new.txt","r")
	tkinter.messagebox.showinfo("PROCESS    ",x.read())
def f5():
	exit()
	
	
root = tkinter.Tk()
root.title("Fancy name")
root.configure(background="black")
root.minsize(500,500)
#root.geometry("150X150")
#root.resizable(0, 0)

scrollbar=Scrollbar(root)
scrollbar.pack( side =RIGHT,fill=Y)

b1=tkinter.Button(root,text="list all files",command=f1)
b2=tkinter.Button(root,text="date",command=f2)
b3=tkinter.Button(root,text="calander",command=f3)
b4=tkinter.Button(root,text="process",command=f4)
B1 = tkinter.Button(root, text ="Exit", relief=RAISED,
                         cursor="spraycan",command=f5)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
B1.pack()

root.mainloop()
