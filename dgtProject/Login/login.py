from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Login")
root.geometry("200x200")

#Functions
#Makes temporary text in entry boxes
def temp_text_u(e):
    """When the username box is selected, if the text is the original prompt (Enter your username) it will become empty to type in."""
    if username_box.get() == "Enter your username":
        username_box.delete(0, "end")
def return_text_u(e):
    """When a user clicks out of/deselects the username box and it's value is blank, it will be filled with the original prompt (Enter your username)."""
    if username_box.get() == "":
        username_box.insert(0, "Enter your username")
def temp_text_p(e):
    """When the password box is selected, if the text is the original prompt (Enter your password) it will become empty to type in."""
    if password_box.get() == "Enter your password":
        password_box.delete(0, "end")
def return_text_p(e):
    """When a user clicks out of/deselects the password box and it's value is blank, it will be filled with the original prompt (Enter your password)."""
    if password_box.get() == "":
        password_box.insert(0, "Enter your password")

#Account
def signup():
    """
    Opens the credentials.txt file in read mode under the name db.
    Stores the values of the username/password entry box in their respective variables.
    Checks if the password length < 6
        If so, it closes the file and displays a warning message
        If not, it shows a success message with the password and its length
    Checks if there are any spaces present in the username or password
        If so, it closes the file and displays a warning message
    """
    db = open("credentials.txt", "r")
    username = username_box.get()
    password = password_box.get()
    if len(password) < 6:
        db.close()
        messagebox.showwarning("Try again", "Password must be at least 6 characters long")
        return
    else:
        messagebox.showinfo("Success", f"Password is {password}\nIt is {len(password)} characters")
    if " " in username or password:
        db.close()
        messagebox.showerror("Try again", "Username and password cannot contain spaces")
        return

def login():
    """
    Stores the values of the username and password box in variables
    Opens the credentials.txt file in read mode
        Loops through the current usernames stored in the file to see if there is a match
        If yes then moves onto password checking step
    """
    username = username_box.get()
    password = password_box.get()
    with open("credentials.txt", "r") as file:
        for i in file:
            if username in file:
                print("user found")
                break
            elif username not in file: 
                print(i)
                print("wrong")
                continue

    # if username_box.get()==username and password_box.get()==password:
    #     pass

def generate_UUID():
    pass

#Creating frames
entry_frame = Frame(root)
entry_frame.grid(row=0, column=0)
button_frame = Frame(root)
button_frame.grid(row=1, column=0)

#Creating entry boxes
username_box = Entry(entry_frame, bg="black", fg="white")
username_box.insert(0, "Enter your username")
username_box.grid(row=1, column=1, pady=20)
password_box = Entry(entry_frame, bg="black", fg="white")
password_box.insert(0, "Enter your password")
password_box.grid(row=2, column=1)
#Binding entry boxes to commands.
username_box.bind("<FocusIn>", temp_text_u)
username_box.bind("<FocusOut>", return_text_u)
password_box.bind("<FocusIn>", temp_text_p)
password_box.bind("<FocusOut>", return_text_p)

var1 = IntVar()

#Buttons
signup_button = Button(button_frame, text="Sign up", command=signup)
signup_button.grid(row=0, column=0, pady=15)
login_button = Button(button_frame, text="Login", command=login)
login_button.grid(row=0, column=1)
remember_button = Checkbutton(button_frame, text="Remember me")
remember_button.grid(row=1, column=0)



root.mainloop()