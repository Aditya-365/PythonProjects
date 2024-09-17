from tkinter import *
import random
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_input.delete(0,END) 
    def Generate_Password() :
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%']

        nr_letters= 6 
        nr_symbols = 1
        nr_numbers = 1

        password_list = []
        for char in range(0,nr_letters) :
            password_list += random.choice(letters)

        for sym in range(0,nr_symbols) :
            password_list += random.choice(symbols)

        for num in range(0,nr_numbers) :
            password_list += random.choice(numbers)

        random.shuffle(password_list)
        password = ""
        for char in password_list :
            password += char
        return password
       
    password_input.insert(0,Generate_Password())

# ------------------------------EXIT----------------------------------- #
def Exit() :
    window.destroy()
# ---------------------------------FIND URL--------------------------------- #
def url() :
    website = website_input.get()
    x = website.split()
    for i in x :
        if i.find(".in") or i.find(".com") or i.find(".org") :
            return True
        else :
            return False
# ------------------------- CONDITIONS ------------------------------------- #
def condition() :
        website = website_input.get()
        email = email_input.get()
        password = password_input.get()
        if len(website) == 0 :
            error = messagebox.showinfo(title="Error",message="You cannot leave website field empty.")
        elif website.endswith((".in",".com",".org")) == False : 
            error = messagebox.showinfo(title="Error",message="You did not enter a valid website.")
        elif len(password) == 0 :
            error = messagebox.showinfo(title="Error",message="You cannot leave password field empty.")
        else :
            return True
# --------------------------GENERATE NEW FILE ------------------------------ #
def New_file() :
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_file_name = new_file_input.get()
    add.config(command=New_file)
    if len(new_file_name) == 0 :
        error = messagebox.showinfo(title="Error",message="You did not enter a valid FileName.")
    with open(f"/Adi/PythonCodes/PasswordManager/{new_file_name}.txt","a") as new_data :
        if condition()  :
            new_data.write(f"\n{website} | {email} | {password}")
            website_input.delete(0,END)
            password_input.delete(0,END)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save() :
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if condition() :
        message = messagebox.askokcancel(title=f"{website}",message=f"These are the details entered :\nE-mail : {email}\nPassword : {password}\nIs it ok to save?" )
        if message :
            with open("/Adi/PythonCodes/PasswordManager/data.txt","a") as data_file :
                data_file.write(f"\n{website} | {email} | {password}")
                website_input.delete(0,END)
                password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")

website_label = Label(text="Website :",fg="black",bg="white",font=("Arial",12,"bold"))
website_label.grid(column=0,row=1)

website_input = Entry(width=47)
website_input.grid(column=1,row=1,columnspan=2)

email_label = Label(text="E-mail :",fg="black",bg="white",font=("Arial",12,"bold"),highlightthickness=0)
email_label.grid(column=0,row=2)
email_input = Entry(width=47)
email_input.grid(column=1,row=2,columnspan=2)
email_entry = email_input.insert(0,"chaditya972@gmail.com")

passsword_label = Label(text="Password :",bg="white",font=("Arial",12,"bold"),highlightthickness=0)
passsword_label.grid(column=0,row=3)
password_input = Entry(fg="black",bg="white",width=29)
password_input.grid(column=1,row=3)


generate_password = Button(text="Generate Password",bg="white",highlightthickness=0,command=generate)
generate_password.grid(column=2,row=3)

add = Button(text="Add",bg="white",highlightthickness=0,width=40,command=save)
add.grid(column=1,row=4,columnspan=2)

Exit = Button(text="Exit",bg="white",highlightthickness=0,width=15,command=Exit)
Exit.grid(column=2,row=4)

new_file_label = Label(text="New_file :",fg="black",bg="white",font=("Arial",12,"bold"),highlightthickness=0)
new_file_label.grid(column=0,row=5)
new_file_input = Entry()
new_file_input.grid(column=1,row=5,columnspan=1)
new_file = Button(text="Generate New File",bg="white",highlightthickness=0,command=New_file)
new_file.grid(column=2,row=5,columnspan=1)

canvas = Canvas(width=200,height=200,highlightthickness=0)
lock_img = PhotoImage(file="/Adi/PythonCodes/PasswordManager/lock2.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)







window.mainloop()