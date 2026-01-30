from database import (
    create_table,
    add_task,
    get_task,
    delete_task
)

def view_task():
    view = get_task()
    if not view:
        print("Nothing to show!")
        return 
    for t in view:
        print(f"{t[0]}. {t[1]} [{t[2]}]")

def main():

    create_table()

    while True:
        print("\n-------TO-Do list---------")
        print("1. Add Task \n2. View Task \n3. Delete Task \n4. Mark Done \n5. Exit")
        user =  int(input("Choose the option (1-5): "))

        if user == 1:
            task = input("Enter the task : ")
            add_task(task)
        elif user == 2:
            view_task()
        elif user == 3:
            print("\n----- Available task ----")
            view_task()
            task_id = int(input("Enter the task ID to delete : "))
            if delete_task(task_id):
                print("\nTask deleted!")
            else:
                print("Task Not Found")
        elif user == 4:
            pass
        elif user == 5:
            print("Good bye!")
            break

if __name__ ==  "__main__":
    main()