import json
import os


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.students = json.load(file)
            except (json.JSONDecodeError, OSError):
                self.students = []
        else:
            self.students = []

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def get_all_students(self):
        return self.students

    def search_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None

    def update_student(self, student_id, updated_data):
        for student in self.students:
            if student["id"] == student_id:
                student.update(updated_data)
                self.save_students()
                return True
        return False

    def delete_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                self.save_students()
                return True
        return False
