from tkinter import *
from tkinter import messagebox
from passwordgenerator import PasswordGenerator

password_generator = PasswordGenerator()
rand_password = password_generator.generate_password()

# print(f"Your password is: {rand_password}")


# password_entry.inset(0, rand_password)

def generate_password():
    rand_password = password_generator.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, rand_password)


password_generator = PasswordGenerator()


def save():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # if not web and not password:
    #     messagebox.showinfo(title="ERROR MESSAGE!!!", message=" Please do not leave any fields empty!")

    # is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} \nPassword:
    # {password}" f" \n Is it ok to save")

    if not web and not password:
        messagebox.showinfo(title="ERROR MESSAGE!!!", message=" Please do not leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password}"
                                               f" \n Is it ok to save")
        if is_ok:
            with open("data.txt", "a") as saved_data:
                saved_data.write(f"Website:{web} |")
                saved_data.write(f"Email:{email} |")
                saved_data.write(f"Password:{password} |")
                saved_data.write("\n")

                # Clear the Entry widgets
                web_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# Label
website = Label(text="Website:")
website.grid(column=1, row=2)

email_user = Label(text="Email/Username:")
email_user.grid(column=1, row=3)

password = Label(text="Password:")
password.grid(column=1, row=4)

# Entry
web_entry = Entry(width=35)
web_entry.grid(column=2, row=2, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "aaden@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

# Button

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=3, row=4)

add = Button(text="Add", width=36, command=save)
add.grid(column=2, row=5, columnspan=2)

window.mainloop()
