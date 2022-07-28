from tkinter import *

window = Tk()
window.minsize(width= 300, height= 120)
value = 0
miles = Label(text="Miles", font=("Arial", 12, 'normal'))
miles.grid(column= 3, row= 1)

def cal():
    value = int(entry.get()) * 1.6
    val = Label(text=value, font=("Arial", 12, 'normal'))
    val.grid(column=2, row=2)

km = Label(text="Km", font=("Arial", 12, 'normal'))
km.grid(column= 3, row= 2)

equal = Label(text="is equal to", font=("Arial", 12, 'normal'))
equal.grid(column= 1, row= 2)

val = Label(text=value, font=("Arial", 12, 'normal'))
val.grid(column=2, row=2)

button = Button(text= "calculate", command= cal)
button.grid(column= 2, row= 3)

entry = Entry()
entry.grid(column= 2, row= 1)



window.mainloop()