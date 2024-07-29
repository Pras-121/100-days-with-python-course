import tkinter
from tkinter import messagebox
import random
import pyperclip as pyclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for char in range(nr_letters)]
    # print(password_list)
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    # print(password_list)
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    # print(password_list)

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    pyclip.copy(password)
    pass_text.insert("1.0", password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_text.get("1.0", "end-1c")
    email = user_text.get("1.0", "end-1c")
    passkey = pass_text.get("1.0", "end-1c")
    line = str(website + " | " + email + " | " + passkey)
    # print(line)
    # messagebox.showinfo(title=, message= )
    if len(website) == 0 or len(passkey) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword:{ passkey}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(line + "\n")
                web_text.delete("1.0", "end-1c")
                pass_text.delete("1.0", "end-1c")


# ---------------------------- UI SETUP ------------------------------- #
tk = tkinter.Tk()
tk.title("Password Manager")
tk.config(padx=60, pady=50)
canvas = tkinter.Canvas(width= 200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# canvas.pack()
canvas.grid(column=1, row=0)
#----- Website Label
web_label = tkinter.Label()
web_label.config(text="Website:  ")
web_label.grid(column=0, row=1)
#-----Website text box
web_text = tkinter.Text(height=1, width=35)
web_text.focus()
web_text.grid(column=1, row=1, columnspan=2)
#----- username Label
uname_label = tkinter.Label()
uname_label.config(text="Email/Username:  ")
uname_label.grid(column=0, row=2)
#-----username text box
user_text = tkinter.Text(height=1,width=35)
user_text.grid(column=1, row=2, columnspan=2)
user_text.insert('1.0', "abc@gmail.com")
#----- password Label
pass_label = tkinter.Label()
pass_label.config(text="Password:   ")
pass_label.grid(column=0, row=3)
#-----password text box
pass_text = tkinter.Text(height=1, width=21)
pass_text.grid(column=1, row=3)
#---- Generate password button
button = tkinter.Button(text="Generate Password", command=gen_password)
button.grid(column=2, row=3)
#----Add button
add = tkinter.Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)





tk.mainloop()