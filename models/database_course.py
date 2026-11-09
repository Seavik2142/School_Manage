from models.course import Course


class DatabaseCourse(Course):
    def __init__(self, course_id , course_name, teacher, database_type):
        super().__init__(course_id, course_name, teacher)
        self.database_type = database_type


    def show_info(self):
        print("---- Database Course Info ----")
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Teacher: {self.teacher.name}")
        print(f"Database Type: {self.database_type}")