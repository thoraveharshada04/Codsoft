import tkinter as tk
from tkinter import messagebox

#MAIN WINDOW
app = tk.Tk()
app.title("To-Do List App")
app.geometry("400x450")
app.resizable(False, False)

tasks = []

# FUNCTIONS 
def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty")
        return
    tasks.append(task)
    listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def update_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to update")
        return
    index = selected[0]
    new_task = task_entry.get()
    if new_task == "":
        messagebox.showwarning("Warning", "Enter updated task")
        return
    tasks[index] = new_task
    listbox.delete(index)
    listbox.insert(index, new_task)
    task_entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to delete")
        return
    index = selected[0]
    listbox.delete(index)
    tasks.pop(index)
    task_entry.delete(0, tk.END)

def show_selected(event):
    selected = listbox.curselection()
    if selected:
        task_entry.delete(0, tk.END)
        task_entry.insert(0, listbox.get(selected))

# UI 
title = tk.Label(app, text="My To-Do List", font=("Arial", 18, "bold"))
title.pack(pady=10)

task_entry = tk.Entry(app, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

btn_frame = tk.Frame(app)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add", width=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(btn_frame, text="Update", width=10, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", width=10, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(app, width=40, height=12)
listbox.pack(pady=15)
listbox.bind("<<ListboxSelect>>", show_selected)

app.mainloop()
