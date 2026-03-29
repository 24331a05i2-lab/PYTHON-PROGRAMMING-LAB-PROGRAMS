import tkinter as tk
from tkinter import messagebox, filedialog
root = tk.Tk()
root.title("GUI Widgets")
root.geometry("400x300")
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
for i in range(1, 21):
    listbox.insert(tk.END, "Item " + str(i))
listbox.pack()
scrollbar.config(command=listbox.yview)
def show_message():
    messagebox.showinfo("Message", "Button Clicked")
btn1 = tk.Button(root, text="Show Message", command=show_message)
btn1.pack()
def open_file():
    filedialog.askopenfilename()
btn2 = tk.Button(root, text="Open File", command=open_file)
btn2.pack()
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Exit", command=root.quit)
mb = tk.Menubutton(root, text="Options")
mb.pack()
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.menu.add_command(label="Option 1")
mb.menu.add_command(label="Option 2")
root.mainloop()