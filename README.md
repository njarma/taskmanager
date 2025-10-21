# TaskManager

TaskManager is a Python-based application for managing tasks. It allows users to add, list, complete, and delete tasks, with all data stored in a JSON file.

## Features

- **Add Tasks**: Create new tasks with unique IDs and descriptions.
- **List Tasks**: View all tasks, including their completion status.
- **Complete Tasks**: Mark tasks as completed.
- **Delete Tasks**: Remove tasks from the list.
- **Persistent Storage**: Tasks are saved to a `tasks.json` file.

## Project Structure

```
TaskManager/
├── ai_service.py          # Placeholder for AI-related features (if any).
├── main.py                # Entry point for the application.
├── README.md              # Project documentation.
├── requirements.txt       # Python dependencies.
├── task_manager.py        # Core logic for task management.
├── tasks.json             # JSON file for storing tasks.
├── test_task_manager.py   # Unit tests for TaskManager.
└── __pycache__/           # Compiled Python files.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/njarma/taskmanager.git
   cd taskmanager
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python3 main.py
```

## Testing

Run the unit tests:
```bash
python3 -m unittest discover -s . -p "test_*.py"
```

## Example

### Adding a Task
```bash
Task added: [ ] 1: Buy groceries
```

### Listing Tasks
```bash
[ ] 1: Buy groceries
[✓] 2: Complete homework
```

### Completing a Task
```bash
Task [✓] 1: Buy groceries -> marked as completed.
```

### Deleting a Task
```bash
Task 1 -> deleted.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

Created by [njarma](https://github.com/njarma).
