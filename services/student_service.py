
"""Student-related application services."""

from models.user import User


class StudentService:

    def __init__(self, student_repository):
        self.student_repository = student_repository

    def register_student(self, student):

        # 1. Validate email
        if not User.is_valid_email(student.email):
            raise ValueError("Invalid email address format.")

        # 2. Check duplicate student ID
        existing_student = self.student_repository.find_student(
            student.user_id
        )

        if existing_student is not None:
            raise ValueError(
                f"Student with ID '{student.user_id}' already exists."
            )

        # 3. Save student
        self.student_repository.add_student(student)

        return True



    
    def update_student(self, student_id, new_name, new_major):

    # 1. Validate name
        if not new_name or not new_name.strip():
            raise ValueError("Name cannot be empty.")

    # 2. Validate major
        if not new_major or not new_major.strip():
            raise ValueError("Major cannot be empty.")

    # 3. Update through repository
        success = self.student_repository.update_student(
            student_id=student_id,
            new_name=new_name.strip(),
            new_major=new_major.strip()
        )

    # 4. Check result
        if not success:
            raise LookupError(
                f"Student ID '{student_id}' not found."
            )

        return True


    def delete_student(self , student_id):
        if not student_id or not str(student_id).strip():
            raise ValueError("Student ID cannot be empty.")

        is_deleted = self.student_repository.delete_student(str(student_id).strip())

        if not is_deleted:
            raise LookupError(f"Can not find student ID: {student_id} for delete.")
        return True

    def get_student(self , student_id):
        if not student_id or not str(student_id).strip():
            raise ValueError("Student ID cannot be empty.")

        student = self.student_repository.find_student(str(student_id).strip())

        if not student:
            raise LookupError(f"Can not find student ID: {student_id}.")

        return student

    def get_all_students(self):
        students = self.student_repository.get_all_students()

        return students