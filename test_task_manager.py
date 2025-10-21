import unittest
from unittest.mock import mock_open, patch
from task_manager import TaskManager, Task
import json

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.mock_tasks = [
            {"id": 1, "description": "Task 1", "completed": False},
            {"id": 2, "description": "Task 2", "completed": True}
        ]
        self.mock_file_data = json.dumps(self.mock_tasks)

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_tasks_file_not_found(self, mock_file):
        with patch("os.path.exists", return_value=False):
            manager = TaskManager()
            self.assertEqual(manager._tasks, {})
            self.assertEqual(manager._next_id, 1)

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_tasks_empty_file(self, mock_file):
        manager = TaskManager()
        self.assertEqual(manager._tasks, {})
        self.assertEqual(manager._next_id, 1)

    @patch("builtins.open", new_callable=mock_open, read_data="[{\"id\": 1, \"description\": \"Task 1\", \"completed\": false}]")
    def test_load_tasks_with_data(self, mock_file):
        manager = TaskManager()
        self.assertEqual(len(manager._tasks), 1)
        self.assertEqual(manager._tasks[1].description, "Task 1")
        self.assertEqual(manager._next_id, 2)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file):
        with patch("task_manager.TaskManager.load_tasks"):
            manager = TaskManager()
            manager._tasks = {
                1: Task(1, "Task 1", False),
                2: Task(2, "Task 2", True)
            }
            manager.save_tasks()

            # Ensure the file was opened for writing
            mock_file.assert_called_once_with(TaskManager.FILENAME, "w")

            # Retrieve the written data
            written_data = "".join(call.args[0] for call in mock_file().write.call_args_list)
            written_json = json.loads(written_data)

            # Validate the written JSON structure
            self.assertEqual(len(written_json), 2)
            self.assertEqual(written_json[0]["description"], "Task 1")
            self.assertEqual(written_json[1]["completed"], True)

if __name__ == "__main__":
    unittest.main()
