from abc import ABC, abstractmethod

class StudentRepositoryInterface(ABC):

    @abstractmethod
    def add_student(self, student):
        pass

    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def find_student(self, student_id):
        pass

    @abstractmethod
    def update_student(self, student_id, new_name, new_major):
        pass

    @abstractmethod
    def delete_student(self, student_id):
        pass