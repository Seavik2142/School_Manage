
from abc import ABC, abstractmethod
from models.teacher import Teacher


class Course(ABC):

    def __init__(self, course_id, course_name, teacher):
        if not self.is_valid_course_id(course_id):
            raise ValueError("Invalid Course ID")

        if not self.is_valid_course_name(course_name):
            raise ValueError("Invalid Course Name")

        if not self.is_valid_teacher(teacher):
            raise TypeError("Teacher must be a Teacher object")

        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher

    @abstractmethod
    def show_info(self):
        pass

    def __str__(self):
        return (
            f"Course ID: {self.course_id}, "
            f"Course Name: {self.course_name}, "
            f"Teacher: {self.teacher.name}"
        )

    @staticmethod
    def is_valid_course_id(course_id):
        return (
            isinstance(course_id, str)
            and course_id.startswith("C")
            and len(course_id) == 5
        )

    @staticmethod
    def is_valid_course_name(course_name):
        return (
            isinstance(course_name, str)
            and 0 < len(course_name.strip()) <= 100
        )

    @staticmethod
    def is_valid_teacher(teacher):
        return isinstance(teacher, Teacher)
