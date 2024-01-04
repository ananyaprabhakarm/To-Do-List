#IMPORTING TKINTER AND MESSAGEBOX
from tkinter import *
import tkinter.messagebox

# CREATING INITIAL WINDOW
window = Tk()
window.title("To-Do")

# FRAME WIDGET
frame = Frame(window)
frame.pack()

# HOLDING ITEMS IN A LISTBOX
listbox = Listbox(frame, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox.pack(side=tkinter.LEFT)

# SCROLLDOWN FUNCTION
scroll = Scrollbar(frame)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

# BUTTONWIDGET
entryButton = Button(window, text="Add Task", width=50)
entryButton.pack(pady=3)

deleteButton = Button(window, text="Delete Selected Task", width=50)
deleteButton.pack(pady=3)

markButton = Button(window, text="Mark as completed", width=50)
markButton.pack(pady=3)

window.mainloop()
