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
    user_input3 = e2.get()
    F=float(user_input3)
    θ=float(user_input2)
    M=float(user_input1)
    Ox=F*sin(radians(θ))
    Oy=(F*cos(radians(θ)))+(M*9.81)-1400
    Mo=(F*cos(radians(θ))*4.8)+(M*9.81*2.4)-(1400*1.2)-15000
    
    result_label.config(text="The resultant at the point 'O' is \nOx : "+format(Ox,' .4f')+" N"+"\nOy : "+format(Oy,' .4f')+" N"+"\nThe moment \
at point 'O' is "+format(Mo,' .4f')+" Nm",font=("Times New Roman",20,"bold"),fg="red",bg="white")
win=Tk()
win.title("Mechanics question 3 by Gagana.P ,SRN=PES1UG23CS214")
win.state("zoomed")
win.config(bg="white")
bgImage=ImageTk.PhotoImage(file="002.jpg")
bglabel=Label(image=bgImage)
bglabel.place(relx=0.5,rely=0.5,anchor="center")
l1=Label(text="Problem based on equilibrium condition",bg="white",font=("Monotype Corsiva",35,"bold"),fg="blue")
l2=Label(text="The uniform beam of mass 'M' is subjected to the three external loads as shown. Compute the reactions at the support point 'O'.\n The x-y plane is vertical. ",bg="white",font=("Times New Roman",25,"bold"))
l3=Label(text="Enter the magnitude of mass of uniform beam in kg : ",bg="white",font=("Times New Roman",20))
l4=Label(text="Enter the magnitude of force 'F1' in newton : ",bg="white",font=("Times New Roman",20))
l5=Label(text="Enter the magnitude of 'θ' in degress: ",bg="white",font=("Times New Roman",20))

e1=Entry(width=10,font=("Times New Roman",20),bd=5,fg="black",bg="white")
e2=Entry(width=10,font=("Times New Roman",20),bd=5,fg="black",bg="white")
entry=Entry(width=10,bd=5,fg="grey",bg="white",font=("Times New Roman",20))

b1=Button(text="submit",bg="white",font=("Times New Roman",20),fg="black",command=calculate_and_print)
result_label = Label(text="")

l1.place(x=600,y=30)
l2.place(x=90,y=150)
l3.place(x=500,y=800)
l4.place(x=500,y=850)
l5.place(x=500,y=900)
e1.place(x=1100,y=800)
e2.place(x=1000,y=850)
entry.place(x=1000,y=900)
entry.insert(0, "0<θ<90")
entry.bind('<FocusIn>', on_entry_click)  
entry.bind('<FocusOut>', on_focus_out)
b1.place(x=900,y=950)

result_label.place(x=1300,y=850)

win.mainloop()
