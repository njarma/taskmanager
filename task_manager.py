import json

class Task:
    def __init__(self, id, description, completed = False):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.description}"
    
class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = {}
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description) -> int:
        task = Task(self._next_id, description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        self.save_tasks()
        print(f"\nTask added: {task}")
        return task.id

    def get_task(self, task_id) -> Task | None:
        return self._tasks.get(task_id, None)

    def list_tasks(self) -> list[Task]:
        if not self._tasks:
            print("\nNo tasks available.")
            return []
        return list(self._tasks.values())

    def complete_task(self, task_id):
        if task_id in self._tasks:
            self.get_task(task_id).mark_completed()
            self.save_tasks()
            print(f"\nTask {self.get_task(task_id)} -> marked as completed.")
        print(f"\nTask {task_id} not found.")
   
    def delete_task(self, task_id):
        if task_id not in self._tasks:
            print(f"\nTask {task_id} not found.")
            return

        del self._tasks[task_id]
        self.save_tasks()
        print(f"\nTask {task_id} -> deleted.")
            
    def load_tasks(self):
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = {
                    int(task_data["id"]): Task(
                        id = int(task_data["id"]),
                        description = task_data["description"],
                        completed = task_data["completed"]
                    )
                    for task_data in data
                }
                if self._tasks:
                    self._next_id = max(self._tasks.keys()) + 1
        except FileNotFoundError:
            self._tasks = {}
            self._next_id = 1
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in tasks file.")
            self._tasks = {}
            self._next_id = 1

    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            json.dump([task.__dict__ for task in self._tasks.values()], file)