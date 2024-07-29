from tkinter import *
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width= 300,height=400)
window.config(padx=20, pady= 20)

input_in="miles"
def onButtonClick():
    user_input = float(textbox.get())
    input_in = listbox.get(listbox.curselection())
    print(input_in)
    if input_in == "miles":
        km_val= round(1.60934 * user_input,1)
        m_val = round(user_input, 1)
        nm_val = round(0.868976* user_input, 1)
        label3.config(text=f"{km_val}")
        label4.config(text=f"{m_val}")
        label6.config(text=f"{nm_val}")
    elif input_in == "Km":
        km_val = round(user_input, 1)
        m_val = round(1/1.60934 * user_input, 1)
        nm_val = round(0.53995 * user_input, 1)
        label3.config(text=f"{km_val}")
        label4.config(text=f"{m_val}")
        label6.config(text=f"{nm_val}")
    elif input_in =="nm":
        km_val = round(1/0.53995 * user_input, 1)
        m_val = round(1 /0.868976 * user_input, 1)
        nm_val = round(user_input, 1)
        label3.config(text=f"{km_val}")
        label4.config(text=f"{m_val}")
        label6.config(text=f"{nm_val}")
#Input
textbox = Entry()
textbox.insert(END,"0")
textbox.grid(column=20, row=1)
textbox.config(width=10)

#"Miles Label
# label1 = Label(text="Miles")
# label1.grid(column=22,row=1)
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
options = ["miles", "Km", "nm"]
for option  in options:
    listbox.insert(options.index(option), option)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=30,row=1)

#"Is equal to" label
label2 = Label(text="is equal to")
label2.grid(column=15,row=10)

# km value label
label3 = Label()
label3.grid(column=20,row=10)
#"km" label
label4 = Label(text="Km")
label4.grid(column=22,row=10)


# Mile value label
label4 = Label()
label4.grid(column=20,row=15)
#"miles" label
label5 = Label(text="miles")
label5.grid(column=22,row=15)


# nm value label
label6 = Label()
label6.grid(column=20,row=25)
#"nm" label
label7 = Label(text="nm")
label7.grid(column=22,row=25)



#"Calculate" button
button = Button(text="Calculate", command=onButtonClick)
button.grid(column=20,row=100)


window.mainloop()
