class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.description}"
    
class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, description) -> int:
        task = Task(self.next_id, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        print(f"\nTask added: {task}")
        return task.id

    def get_task(self, task_id) -> Task | None:
        return self.tasks.get(task_id, None)

    def list_tasks(self) -> list[Task]:
        if not self.tasks:
            print("\nNo tasks available.")
            return []
        return list(self.tasks.values())

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.get_task(task_id).mark_completed()
            print(f"\nTask {self.get_task(task_id)} -> marked as completed.")
        print(f"\nTask {task_id} not found.")
   
    def delete_task(self, task_id):
        if task_id not in self.tasks:
            print(f"\nTask {task_id} not found.")
            return

        del self.tasks[task_id]
        print(f"\nTask {task_id} -> deleted.")
            