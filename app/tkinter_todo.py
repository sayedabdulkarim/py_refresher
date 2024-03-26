import tkinter as tk
from tkinter import simpledialog

def add_task():
    task = simpledialog.askstring("Input", "Enter a new task:")
    if task:
        listbox_tasks.insert(tk.END, task)

def delete_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        listbox_tasks.delete(selected_task)

def show_tasks():
    # This function can be used to show tasks if they are not always visible
    pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display tasks
listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

# Create buttons for adding and deleting tasks
button_add_task = tk.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

# Run the main loop
root.mainloop()
