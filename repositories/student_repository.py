"""Student data repository."""

class StudentRepository:

    def __init__(self):
        self.students = []

    # CREATE
    def add_student(self, student):
        if self.find_student(student.user_id):
            raise ValueError("Student ID already exists.")

        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    # READ ALL
    def get_all_students(self):
        return self.students

    # READ ONE
    def find_student(self, student_id):
        for student in self.students:
            if student.user_id == student_id:
                return student

        return None

    # UPDATE
    def update_student(self, student_id, new_name, new_major):
        student = self.find_student(student_id)

        if student is None:
            return False

        if new_name is not None:
            student.name = new_name

        if new_major is not None:
            student.major = new_major

        return True

    # DELETE
    def delete_student(self, student_id):
        student = self.find_student(student_id)

        if student is None:
            return False

        self.students.remove(student)
        print(f"Student {student_id} deleted successfully.")
        return True