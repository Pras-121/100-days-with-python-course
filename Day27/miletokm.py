from tkinter import *
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width= 300,height=200)
window.config(padx=20, pady= 20)


def onButtonClick():
    input_in_miles = float(textbox.get())
    input_in_km = round(1.60934 * input_in_miles,1)
    label3.config(text=f"{input_in_km}")
#Input
textbox = Entry()
textbox.insert(END,"0")
textbox.grid(column=20, row=1)
textbox.config(width=10)

#"Miles Label
label1 = Label(text="Miles")
label1.grid(column=22,row=1)
#"Is equal to" label
label2 = Label(text="is equal to")
label2.grid(column=15,row=3)
# km value label
label3 = Label()
label3.grid(column=20,row=3)
#"km" label
label4 = Label(text="Km")
label4.grid(column=22,row=3)
#"Calculate" button
button = Button(text="Calculate", command=onButtonClick)
button.grid(column=20,row=10)


window.mainloop()
