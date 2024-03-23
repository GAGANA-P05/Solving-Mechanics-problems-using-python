from tkinter import *
from math import *
from PIL import ImageTk
def on_entry_click(event):
    if entry.get() == "F1>F2":
        entry.delete(0, END)
        entry.config(fg='black')  
def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "F1>F2")
        entry.config(fg='grey')
def on_entry(event):
    if e1.get() == "F1>F2":
        e1.delete(0, END)
        e1.config(fg='black')  
def on_focus(event):
    if e1.get() == "":
        e1.insert(0, "F1>F2")
        e1.config(fg='grey')       
def calculate_and_print():
    user_input2 = entry.get()
    user_input1 = e1.get()
    F1=float(user_input1)
    F2=float(user_input2)
    a=F1-F2
    w2=(a*0.5)*6
    w1=F2*8
    Rb =((w2*2)+(w1*4))/7
    Ra=w1+w2-Rb    
    result_label.config(text="The reaction at 'A' is : "+format(Ra,' .4f')+" N"+"\n The reaction at 'B' is : "+format(Rb,' .4f')+" N",font=("Times New Roman",20,"bold"),fg="red",bg="white")
win=Tk()
win.title("Mechanics question 2 by Gagana.P ,SRN=PES1UG23CS214")
win.state("zoomed")
win.config(bg="white")
bgImage=ImageTk.PhotoImage(file="001.jpg")
bglabel=Label(image=bgImage)
bglabel.place(relx=0.5,rely=0.5,anchor="center")
l1=Label(text="Problem based on external effects of beams",bg="white",font=("Monotype Corsiva",35,"bold"),fg="blue")
l2=Label(text="Determine the reactions at the supports of the beam(A and B) which is loaded as shown.",bg="white",font=("Times New Roman",25,"bold"))
l3=Label(text="Enter the magnitude of uniformly varing load F1 in 'Nm': ",bg="white",font=("Times New Roman",20))
l4=Label(text="Enter the magnitude of uniformly distributed F2 load in 'Nm': ",bg="white",font=("Times New Roman",20))
e1=Entry(width=10,font=("Times New Roman",20),bd=5,fg="grey",bg="white")
entry=Entry(width=10,bd=5,fg="grey",bg="white",font=("Times New Roman",20))
b1=Button(text="submit",bg="white",font=("Times New Roman",20),fg="black",command=calculate_and_print)
result_label = Label(text="")
l1.place(x=600,y=30)
l2.place(x=90,y=150)
l3.place(x=450,y=800)
l4.place(x=450,y=850)
e1.place(x=1110,y=800)
entry.place(x=1170,y=850)
b1.place(x=900,y=900)
entry.insert(0, "F1>F2")
entry.bind('<FocusIn>', on_entry_click)  
entry.bind('<FocusOut>', on_focus_out)
e1.insert(0, "F1>F2")
e1.bind('<FocusIn>', on_entry)  
e1.bind('<FocusOut>', on_focus)
result_label.place(x=1300,y=850)
win.mainloop()
