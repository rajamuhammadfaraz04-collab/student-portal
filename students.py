import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "students.json"


def load_students() -> list[dict]:
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_students(students: list[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)


def add_student(name: str, age: int, student_id: str) -> dict:
    students = load_students()
    student = {
        "name": name,
        "age": age,
        "student_id": student_id,
    }
    students.append(student)
    save_students(students)
    return student


if __name__ == "__main__":
    name = input("Student name: ").strip()
    age = int(input("Student age: ").strip())
    student_id = input("Student ID: ").strip()

    student = add_student(name, age, student_id)
    print(f"Saved student: {student}")
