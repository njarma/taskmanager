from task_manager import TaskManager

def print_menu():
    print("\n~ Task manager menu ~")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def get_user_choice() -> int:
    return int(input("\nEnter your choice: "))

def get_task_id(message: str) -> int:
    return int(input(message))

def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = get_user_choice()

        try:      
            match choice:
                case 1:
                    description = input("Enter task description: ")
                    task_manager.add_task(description)
                    continue
                case 2:
                    tasks = task_manager.list_tasks()
                    for task in tasks:
                        print(task)
                    continue
                case 3:
                    task_id = get_task_id(message="Enter task ID to complete: ")
                    task_manager.complete_task(task_id)
                case 4:
                    task_id = get_task_id(message="Enter task ID to delete: ")
                    task_manager.delete_task(task_id)
                case 5:
                    print("Exiting task manager....")
                    break
                case _:
                    print("Invalid choice. Please try again.")
                    continue
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()