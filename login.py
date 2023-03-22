from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#colors
color1 = "white"
color2 = "black"
color3 = "#6074FF"

window = Tk()
window.title("testing login")
window.geometry('310x300')
window.resizable(width = False, height = False)
window.configure(background = color1)

#credentials
credentials = ['Testeng', 'Testval1']

def check_login():
    login_name = e_name.get()
    login_password = str(e_password.get())

    if login_name == 'admin' and login_password == 'admin':
        messagebox.showinfo('Login', 'Welcome Admin')

    elif login_name == credentials[0] and login_password == credentials[1]:
        messagebox.showinfo('Login', 'Welcome Back ' + credentials[0])

        for widget in frame_down.winfo_children():
            widget.destroy()

        for widget in frame_down.winfo_children():
            widget.destroy()

        new_window()
    else:
        messagebox.showwarning('Error', 'Invalid username or password')

def new_window():
    username = Label(frame_down, text="name *", height=1, background=color1, anchor=NW, foreground=color2, font=('Poppins 12 bold'))
    username.place(x=10, y=10)

    username = Label(frame_down, text="Welcome " + credentials[0], height=1, background=color1, anchor=NW, foreground=color2,font=('Poppins 12 bold'))
    username.place(x=10, y=10)


frame_up = Frame(window, width = 310, height = 50, background = color1)
frame_up.grid(row = 0, column = 0)

frame_down = Frame(window, width = 310, height = 300, background = color1)
frame_down.grid(row = 1, column = 0)

#frame_up widgets
heading = Label(frame_up, text = "LOGIN", background = color1, font = ('Poppins 23'))
heading.place(x = 5, y = 5)

line = Label(frame_up, width = 47, text = "", height = 1, background = color3, anchor = NW)
line.place(x = 10, y = 45)

#frame_down widgets
username = Label(frame_down, text = "name *", height = 1, background = color1, anchor = NW, foreground = color2, font = ('Poppins 12 bold'))
username.place(x = 10, y = 10)

e_name = Entry(frame_down, width = 25, justify = 'left', font = ("", 15), highlightthickness = 1)
e_name.place(x = 14, y = 48)

password = Label(frame_down, text = "password *", height = 1, background = color1, anchor = NW, foreground = color2, font = ('Poppins 12 bold'))
password.place(x = 10, y = 100)

e_password = Entry(frame_down, width = 25, justify = 'left', font = ("", 15), highlightthickness = 1, show = '?')
e_password.place(x = 14, y = 140)

#button
button_confirm = Button(frame_down, text = "Login", background = color3, foreground = color1, width = 29, height = 2, font = ("Ivy 9 bold"), command = check_login)
button_confirm.place(x = 40, y = 180)

window.mainloop()
