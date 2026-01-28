import os

file_name = "task_list.txt"

def load_task():
    if not os.path.exists(file_name):
        return []
    
    with open(file_name,"r") as f:
        tasks = f.read().splitlines()
    return tasks

def save_task(tasks):
    with open(file_name, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task : ").strip()

    if task:
        tasks.append(task)
        save_task(tasks)
        print("Task Updated.")
    else:
        print("Empty task not allowed.")

def view(tasks):
    if not tasks:
        print("No task found!")
        return
    print("\n-------Task List-------")
    for i , task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(tasks):
    print("\n-------Task List-------")
    view(tasks)
    if not tasks:
        print("Task list is empty!")
        return
    
    index = int(input("Enter the number for delete task: "))
    if 1<= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_task(tasks)
        print(f"Deleted : {removed}")
    else:
        print("Invalid task number!")

def main():
    tasks = load_task()
    
    while True:
        print("\n--------To-Do list--------")
        print("1. Add Task \n2. View Task \n3. Delete Task \n4. Exit")
        user = int(input("Enter what you want you do : "))

        if user ==  1:
            add_task(tasks)
        elif user == 2:
            view(tasks)
        elif user == 3:
            delete_task(tasks)
        elif user == 4:
            break
        else:
            print("Enter the choice b/w (1-4)")
            

if __name__ == "__main__":
    main()