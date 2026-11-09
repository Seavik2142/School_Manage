from models.course import Course

class ProgrammingCourse(Course):
    def __init__(self, course_id, course_name, teacher, programming_language):
        super().__init__(course_id, course_name, teacher)
        self.programming_language = programming_language

    def show_info(self):
        print("---- Programming Course Info ----")
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Teacher: {self.teacher.name}")
        print(f"Programming Language: {self.programming_language}")