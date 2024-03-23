from tkinter import *
from math import *
from PIL import ImageTk

def on_entry_click(event):
    if entry.get() == "0<θ<90":
        entry.delete(0, END)
        entry.config(fg='black')  

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "0<θ<90")
        entry.config(fg='grey')
        
def calculate_and_print():
    user_input2 = entry.get()
    user_input1 = e1.get()
    F=float(user_input1)
    θ=float(user_input2)
    result=abs((F*sin(radians(θ))*0.03)-(F*cos(radians(θ))*0.2))
    result_label.config(text="The moment at the point 'O'\n is : "+format(result,' .4f')+" Nm in Clockwise direction",font=("Times New Roman",20,"bold"),fg="red",bg="white")




win=Tk()
win.title("Mechanics question 1 by Gagana.P ,SRN=PES1UG23CS214")
win.state("zoomed")
win.config(bg="white")
bgImage=ImageTk.PhotoImage(file="screenshot.jpg")
bglabel=Label(image=bgImage)
bglabel.place(relx=0.5,rely=0.5,anchor="center")
l1=Label(text="Problem based on moment",bg="white",font=("Monotype Corsiva",35,"bold"),fg="blue")
l2=Label(text="Calculate the moment of the force 'F' newton acting at an angle of θ on the handle of the monkey wrench about the center\nof the bolt. [0<θ<90]",bg="white",font=("Times New Roman",25,"bold"))
l3=Label(text="Enter the magnitude of force 'F' in Newton: ",bg="white",font=("Times New Roman",20))
l4=Label(text="Enter the value of 'θ' in degrees: ",bg="white",font=("Times New Roman",20))
e1=Entry(width=10,font=("Times New Roman",20),bd=5,fg="black",bg="white")
entry=Entry(width=10,bd=5,fg="grey",bg="white",font=("Times New Roman",20))

b1=Button(text="submit",bg="white",font=("Times New Roman",20),fg="black",command=calculate_and_print)
result_label = Label(text="")

l1.place(x=680,y=30)
l2.place(x=50,y=150)
l3.place(x=500,y=800)
l4.place(x=500,y=850)
e1.place(x=980,y=800)
entry.place(x=980,y=850)
b1.place(x=900,y=900)

entry.insert(0, "0<θ<90")
entry.bind('<FocusIn>', on_entry_click)  
entry.bind('<FocusOut>', on_focus_out)
result_label.place(x=1300,y=850)

win.mainloop()
