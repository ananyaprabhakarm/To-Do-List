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
listbox = Listbox(frame, bg="white", fg="black", height=15, width=50, font="Helvetica")
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

# TO DO FUNCTIONS
def entertask():
  input = ""
  def add():
    input = entry.get(1.0, "end-1c")
    if input == "":
      tkinter.messagebox.showwarning(title="Warning!" ,message="Enter the text")
    else:
      listbox.insert(END,input)
      root1.destroy()

root1 = Tk()
root1.title("Add Task")
entry = Text(root1, width=40, height=4)
entry.pack()
button = Button(root1, text="Add Task")
button.pack()
root1.mainloop()


def deletetask():
  select = listbox.curselection()
  listbox.delete(select[0])


def markscomplete():
  mark = listbox.curselection()
  temp = mark[0]

  marked = listbox.get(mark)

  marked = marked + " ✔"

  listbox.delete(temp)
  listbox.insert(temp,marked)