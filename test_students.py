import json
import tempfile
import unittest
from pathlib import Path

import students


class StudentsPersistenceTest(unittest.TestCase):
    def test_add_student_saves_data(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            original_data_file = students.DATA_FILE
            students.DATA_FILE = Path(tmpdir) / "students.json"
            try:
                students.add_student("Alice", 20, "S001")
                students.add_student("Bob", 22, "S002")

                self.assertTrue(students.DATA_FILE.exists())
                with students.DATA_FILE.open("r", encoding="utf-8") as file:
                    data = json.load(file)

                self.assertEqual(
                    data,
                    [
                        {"name": "Alice", "age": 20, "student_id": "S001"},
                        {"name": "Bob", "age": 22, "student_id": "S002"},
                    ],
                )
            finally:
                students.DATA_FILE = original_data_file


if __name__ == "__main__":
    unittest.main()
