import tkinter as tk
from tkinter import messagebox

class TodoApp:  
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("300x350")

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10, padx=10, anchor="w")

        # Button Frame (for left alignment)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(anchor="w", padx=10)

        # Add Task Button (Left-aligned)
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=2, fill="x")

        # Mark Completed Button (Left-aligned)
        self.complete_button = tk.Button(self.button_frame, text="Mark Completed", command=self.mark_completed)
        self.complete_button.pack(pady=2, fill="x")

        # Save to File Button (Left-aligned)
        self.save_button = tk.Button(self.button_frame, text="Save to File", command=self.save_to_file)
        self.save_button.pack(pady=2, fill="x")

        # Task Listbox
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10, padx=10, anchor="w")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "iscompleted": False})
            self.listbox.insert(tk.END, f"[ ] {task}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def mark_completed(self):
        try:
            selected_index = self.listbox.curselection()[0]
            task_text = self.listbox.get(selected_index)
            self.tasks[selected_index]["iscompleted"] = True
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, f"[✓] {self.tasks[selected_index]['task']}")
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def save_to_file(self):
        with open("todo.txt", "w") as f:
            for task in self.tasks:
                f.write(f"{task['task']}, {task['iscompleted']}\n")
        messagebox.showinfo("Saved", "Tasks saved to file!")

# Run the application
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
