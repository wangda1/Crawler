#-*-coding=utf-8-*-
#
#This is the first page for commicuating with the user
#Time:2017.3.31.N

from tkinter import *



root=Tk()
root.title("Python-Crawler")
root['width']=1000
root['height']=500

f1=Frame();f1.pack()
f2=Frame();f2.pack()
f3=Frame();f3.pack()

l1=Label(f1,text="URL")
l1.pack(side='left')
e1=Entry(f1)
#e1.bind("<Button-1>")
e1.pack()

l2=Label(f2,text="keywords")
l2.pack(side='left')
e2=Entry(f2)
e2.pack()


l3=Label(f3,text="number")
l3.pack(side='left')
e3=Entry(f3)
e3.pack()

bt1=Button(root)
bt1["text"]="Run"
bt1.pack()


root.mainloop()

























