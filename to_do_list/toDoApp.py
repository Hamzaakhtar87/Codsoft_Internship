import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do list Application")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command = self.add_task, bg="white", fg="black")
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=60, height=30)
        self.task_listbox.grid(row=1, column=0,columnspan=5, padx=10, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="white", fg="black")
        self.remove_button.grid(row=2, column=0,padx=10, pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, bg="white", fg="black")
        self.quit_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0,tk.END)

    def remove_task(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            removed_task = self.tasks.pop(index)
            messagebox.showinfo("Task Removed", f"'{removed_task}' has been removed!")
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()