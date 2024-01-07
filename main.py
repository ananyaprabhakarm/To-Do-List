#IMPORTING TKINTER AND MESSAGEBOX
from tkinter import *
import tkinter.messagebox


# TO DO FUNCTIONS
def entertask():
  user_input = ""
  def add():
    user_input = entry.get(1.0, "end-1c")
    if user_input == "":
      tkinter.messagebox.showwarning(title="Warning!" ,message="Enter the text")
    else:
      listbox.insert(END, user_input)
      entry.delete(0, END)

  root1 = Toplevel()
  root1.title("Add Task")
  entry = Text(root1, width=40)
  entry.pack()
  button = Button(root1,width=40, height=2,text="Add", command=add)
  button.pack()
  root1.mainloop()
      
def deletetask():
  select = listbox.curselection()
  listbox.delete(select)

def markscomplete():
  mark = listbox.curselection()
  temp = mark[0]
  marked = listbox.get(mark)
  marked = marked + " ✔"
  listbox.delete(temp)
  listbox.insert(temp,marked)

# CREATING WINDOW
root = Tk()
root.title("To-Do")

# FRAME WIDGET
frame = Frame(root)
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
entryButton = Button(root, text="Add Task", width=50, command=entertask)
entryButton.pack(pady=3)
deleteButton = Button(root, text="Delete Selected Task", width=50, command=deletetask)
deleteButton.pack(pady=3)
markButton = Button(root, text="Mark as completed", width=50, command=markscomplete)
markButton.pack(pady=3)

root.mainloop()




