from tkinter import *
def show():
    print(entry.get())
root = Tk()
root.title("Hello App")
root.geometry("300x200")
label = Label(root, text="Enter Name")
label.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text="Submit", command=show)
button.pack()
root.mainloop()