from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Project 1")
root.geometry("300x300")
icon=PhotoImage(file='icon.png')
root.iconphoto(True,icon)

def submit():
    a=entry1.get()
    print('Student name is :',a)
    b=entry2.get()
    print('Class is :',b)

label=Label(text='Name',font=('Times New Roman',14,'italic'))
label.place(x=0,y=0)

entry1=Entry()
entry1.place(x=60,y=5)

label=Label(text='Class',font=('Times New Roman',14,'italic'))
label.place(x=0,y=28)

entry2=Entry()
entry2.place(x=60,y=30)

button=Button(text="Click to Exit",font=("Arial",12,"bold"),command=quit)
button.place(x=85,y=85)

button=Button(text="Submit",font=("Arial",12,"bold"),command=submit)
button.place(x=5,y=85)

check_button=Checkbutton(text='Do you accept every rules')
check_button.place(x=5,y=55)

root.mainloop()