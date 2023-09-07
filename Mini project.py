import tkinter as tk
from tkinter import messagebox

# Hardcoded username and password
USERNAME = "Divya"
PASSWORD = "1234"

# Function to check authentication
def authenticate():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == USERNAME and password == PASSWORD:
        login_window.destroy()
        create_todo_list()

    else:
        messagebox.showerror("Authentication Error", "Invalid username or password")

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Username label and entry
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

# Password label and entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(login_window, text="Login", command=authenticate)
login_button.pack()

# Main function to create the to-do list window
def create_todo_list():
    def add_task():
        task = task_entry.get()
        if task:
            todo_list.insert(tk.END, task)
            task_entry.delete(0, tk.END)

    def delete_task():
        try:
            selected_task_index = todo_list.curselection()[0]
            todo_list.delete(selected_task_index)
        except IndexError:
            pass

    # Create the to-do list window
    todo_window = tk.Tk()
    todo_window.title("To-Do List")

    # Task entry and add button
    task_entry = tk.Entry(todo_window)
    task_entry.pack()
    add_button = tk.Button(todo_window, text="Add Task", command=add_task)
    add_button.pack()

    # To-do list
    todo_list = tk.Listbox(todo_window)
    todo_list.pack()

    # Delete button
    delete_button = tk.Button(todo_window, text="Delete Task", command=delete_task)
    delete_button.pack()

    todo_window.mainloop()

login_window.mainloop()
