
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

def save_data():
    sentiment = selection_var.get()
    dayOfWeek = day_scale.get()
    steps = step_count.get()
    notes = notes_box.get("1.0", "end")
    dogfed = checked.get()

    writeFile = open("GUI_Input.txt", "a")
    writeFile.write(sentiment + "," + dayOfWeek + "," + steps + "," + dogfed + "," + notes)
    writeFile.close()
    tk.messagebox.showinfo("Daily Tracker","Saved!")

#creates the window for the GUI
root = tk.Tk()
root.geometry("600x450")
root.resizable(True, True)
root.title("Daily Tracker")

#set style
rootStyle = ttk.Style(root)
rootStyle.theme_use(None)

#creates radio buttons for user sentiment
selection_var = tk.StringVar()
upset = ttk.Radiobutton(
    root,
    text = "Upset",
    variable=selection_var,
    value="Upset")
excited = ttk.Radiobutton(
    root,
    text = "Excited",
    variable=selection_var,
    value="Excited")
anxious = ttk.Radiobutton(
    root,
    text = "Anxious",
    variable=selection_var,
    value="Anxious")
calm = ttk.Radiobutton(
    root,
    text = "Calm",
    variable=selection_var,
    value="Calm")
happy = ttk.Radiobutton(
    root,
    text = "Happy",
    variable=selection_var,
    value="Happy")

#labels buttons
sentiment_label=ttk.Label(root,text="How are you feeling today?")

#places buttons on grid
sentiment_label.place(x=20, y=20)
happy.place(x=100,y=40)
calm.place(x=200,y=40)
anxious.place(x=300,y=40)
excited.place(x=400,y=40)
upset.place(x=500,y=40)

#labels combo box
day_box_label=ttk.Label(root,text="What day of the week is it?")

#places lable
day_box_label.place(x=20,y=70)

#creates comobox
day_scale = tk.StringVar()
day_box = ttk.Combobox(root, textvariable=day_scale)
day_box["values"] = ("Monday","Tuesday", "Wednesday", "Thursday","Friday","Saturday", "Sunday")
day_box.place(x=20,y=90)

#creates and lables and entry box
step_count = tk.StringVar()
step_box_label=ttk.Label(root,text="How many steps did you get in today?")
step_box_label.place(x=20,y=110)

step_entry = ttk.Entry(root, width=15, textvariable=step_count)
step_entry.place(x=20, y=130)
step_entry.focus()


#creates and places a text box
notes_box = tk.Text(root, height=6)
notes_box.place(x=20,y=160)
notes_box.insert("1.0", "enter any notes about your day here...")

#adding an image
doggo = Image.open("IMG_0757.png").resize((80, 100))
doggo_image = ImageTk.PhotoImage(doggo)
ttk.Label(root,text="Did you feed the dog today?", image=doggo_image, compound="left", padding=5).place(x=20,y=250)

#checkbox for feeding dog
checked = tk.StringVar()
fed_checkbox = ttk.Checkbutton(root, variable=checked, onvalue="Fed", offvalue="not fed", text="Dog was fed!").place(x=150, y=320)

#creates a button that quits program

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.place(x=500,y=350)

save_data_button = ttk.Button(root, text="Save Data", command=save_data)
save_data_button.place(x=375,y=350)

root.mainloop()
