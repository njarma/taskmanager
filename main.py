from task_manager import TaskManager

def main():
    task_manager = TaskManager()

    while True:
        print("\n~ Task manager menu ~")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                description = input("Enter task description: ")
                task_manager.add_task(description)
                continue
            case "2":
                tasks = task_manager.list_tasks()
                for task in tasks:
                    print(task)
                continue
            case "3":
                try:
                    task_id = int(input("Enter task ID to complete: "))
                    task_manager.complete_task(task_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")
                continue
            case "4":
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    task_manager.delete_task(task_id)
                except ValueError:
                    print("Invalid ID. Please enter a number.")
                continue
            case "5":
                print("Exiting Task Manager....")
                break
            case _:
                print("Invalid choice. Please try again.")
                continue

if __name__ == "__main__":
    main()