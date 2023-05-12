
                 ##### UI DESIGN (POPUP) FOR AUTHENTICATION ######

# tkinter library of python to design popup
import tkinter as tk
from tkinter import simpledialog


def popup():
    answer = tk.messagebox.askquestion("USB not authenticated",
    "Do you want to allow the device to access your computer?", icon='warning', type='yesno')

    if answer == 'yes':
        password = simpledialog.askstring("Password", "Enter password:")
        if password=='123':
            from auth import connected
            tk.messagebox.showinfo("Authentication status", "Device Authenticated")
            ## correct password -> considered authenticated ###
        else:
            tk.messagebox.showwarning("Authentication status","Password incorrect")
            ## incorrect password -> not authenticated ###
    else:
        tk.messagebox.showinfo("showinfo", "Device ejected")

root = tk.Tk()
root.withdraw()

popup()
