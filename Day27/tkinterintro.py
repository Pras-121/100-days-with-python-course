from tkinter import *

def button_click():
    label["text"] = input.get()


window = Tk()
window.title("GUI Program")
window.minsize(width= 600,height=600)
window.config(padx=20, pady= 20)
#Label
label = Label(text="Hi, I am Label", font=("Arial", 24, "normal"))
# label.pack()
# label.place(x=0,y=0) // Precises positioning
label.grid(column=0, row=0)
#Button
button1 = Button(text="Click me", command=button_click)
# button.pack()
button1.grid(column=1, row=1)

#Entry
input = Entry(width=10)
input.insert(END,"Type Here")
# input.pack()
input.grid(column=4, row=2)

button2 = Button(text="Button2")
button2.grid(column=2,row=0)

#Text Entry box
# text = Text(height=5, width=30)
# text.focus()
# text.insert(END, "Example of a multi line text.")
#text.get()
# text.pack()
#spinbox
#Scale (slider)
#checkbox
#radiobutton
#Listbox
window.mainloop()
