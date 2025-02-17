class Todo:
    def __init__(self, task, iscompleted):
        self.task = task
        self.iscompleted = iscompleted

    def display(self):
        if self.iscompleted:
            print(f"{self.task} is completed")
        else:
            print(f"{self.task} is pending")

    def save_tofile(self):
        with open("todo.txt", "a") as f:
            f.write(f"{self.task}, {self.iscompleted}\n")    

todos = []
while True:
    task = input("Enter the task: ")
    iscompleted = input("Is the task completed? (y/n): ")
    if iscompleted == "y":
        iscompleted = True
    else:
        iscompleted = False
    todo = Todo(task, iscompleted)
    todo.save_tofile()
    todos.append(todo)
   
    choice = input("Do you want to add more? (y/n): ")
    if choice.lower() == "n":
        break


for todo in todos:
    todo.display()