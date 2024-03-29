from task_list import TaskList
from task import Task

def main():
    task_list = TaskList()

    while True:
        print("1. Add task")
        print("2. Update task status")
        print("3. Remove task")
        print("4. Display all tasks")
        print("5. Task filter")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_id = input("Enter task ID: ")
            title = input("Enter title: ")
            description = input("Enter description: ")
            status = input("Enter status: ")
            due_date = input("Enter due date: ")

            new_task = Task(task_id, title, description, status, due_date)
            task_list.add(new_task)

            print("Task added successfully.\n")

        elif choice == '2':
            task_id = input("Enter task ID to update status: ")
            new_status = input("Enter new status: ")

            for task in task_list.data:
                if task.id == task_id:
                    task.change_status(new_status)
                    print("Task status updated.\n")
                    break
            else:
                print(f"Task with ID {task_id} not found.\n")

        elif choice == '3':
            task_id = input("Enter task ID to remove: ")
            task_list.remove(task_id)

        elif choice == '4':
            task_list.show()

        elif choice == '5':
            status = input("Enter status to filter tasks: ")
            task_list.show(status)

        elif choice == '6':
            print("Exit.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
