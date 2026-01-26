def load_task():
    pass
def add_task():
    task = input("Enter the task : ")

    with open("task_list.txt", "a") as f:
        f.write(task + "\n")


def view():
    pass

def delete_task(tasks):
    pass

def main():
    print("--------To-Do list--------")
    print("1. Add Task \n2. View Task \n3. Delete Task")
    user = int(input("Enter what you want you do : "))

    if user ==  1:
        add_task()

if __name__ == "__main__":
    main()