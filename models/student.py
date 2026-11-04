from models.user import User

class Student(User):
    def __init__(self, user_id, name, email, password, major):
        super().__init__(user_id, name, email, password)
        self.major = major
        self.courses = []



    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} has enrolled in {course.course_name}.")

    def show_info(self):
        print("-----Student Information-----")
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Major: {self.major}")   
        print(f"courses: {len(self.courses)}")