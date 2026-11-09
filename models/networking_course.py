
from models.course import Course


class NetworkingCourse(Course):

    def __init__(self, course_id, course_name, teacher, network_tool):
        super().__init__(course_id, course_name, teacher)
        self.network_tool = network_tool

    def show_info(self):
        print("---- Networking Course Info ----")
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Teacher: {self.teacher.name}")
        print(f"Network Tool: {self.network_tool}")
