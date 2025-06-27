import numpy as np
import tkinter as tk



# Create the main app window
root = tk.Tk()
root.title("Todo List")
root.geometry("400x400")

label = tk.Label(root, text="hello world!")
label.pack()  # Arranges the widget within the window

# Task list
tasks = []
# Functions
def add_task():
    item_to_add = entry.get()
    tasks.append(item_to_add)
    update_tasks()

def deleteTask():
    itemToRemove = input("Enter item to delete: ")
    if itemToRemove in tasks:
        tasks.remove(itemToRemove)
        print("Item removed from list")
    else:
        print("Item not found in list")
        
def update_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
        
# Entry widget
entry = tk.Entry(root, font='Helvetica')
entry.pack(pady=20)

# Add button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

# Listbox to show tasks
listbox = tk.Listbox(root)
listbox.pack()

# Delete button


# Start the GUI event loop
tk.mainloop()
