
# from models.student import Student
# from models.teacher import Teacher
# from models.user import User


# student = Student(
#     "S001",
#     "Mao Seavik",
#     "seavik@example.com",
#     "password123",
#     "Computer Science"
# )

# teacher = Teacher(
#     "T001",
#     "John",
#     "john@example.com",
#     "password456",
#     "IT Department"
# )


# users = [student, teacher]

# for user in users:
#     user.show_info()
#     print()


# User.show_total_users()

# print(student)
# print(student.verify_password("password123"))
# print(User.is_valid_email("seavik@example.com"))


#_________________________________________________________#







# from models.teacher import Teacher
# from models.programming_course import ProgrammingCourse
# from models.database_course import DatabaseCourse
# from models.networking_course import NetworkingCourse


# teacher = Teacher(
#     "T001",
#     "John",
#     "john@example.com",
#     "password123",
#     "IT Department"
# )

# python_course = ProgrammingCourse(
#     "C0001",
#     "Python OOP",
#     teacher,
#     "Python"
# )

# database_course = DatabaseCourse(
#     "C0002",
#     "Database Management",
#     teacher,
#     "PostgreSQL"
# )

# network_course = NetworkingCourse(
#     "C0003",
#     "Computer Networking",
#     teacher,
#     "Cisco Packet Tracer"
# )

# courses = [
#     python_course,
#     database_course,
#     network_course
# ]

# for course in courses:
#     course.show_info()
#     print()




#________________________________________________________#



from models.student import Student
from repositories.student_repository import StudentRepository


# Create Student Objects
student1 = Student(
    "S001",
    "Seavik",
    "seavik@example.com",
    "password123",
    "Computer Science"
)

student2 = Student(
    "S002",
    "Dara",
    "dara@example.com",
    "password456",
    "Software Engineering"
)


# Create Repository
repository = StudentRepository()


# CREATE
repository.add_student(student1)
repository.add_student(student2)


# READ ALL
print("\n----- All Students -----")

for student in repository.get_all_students():
    student.show_info()
    print()


# READ ONE
print("----- Search Student -----")

result = repository.find_student("S001")

if result:
    result.show_info()
else:
    print("Student not found!")

# UPDATE
print("----- Update Student -----")
success = repository.update_student("S001", "Seavik Mao", "Cybersecurity")

if success:
    print("Update successful!\n")
else:
    print("Student not found!\n")


# DELETE
print("----- Delete Student -----")
deleted = repository.delete_student("S002")

if deleted:
    print("Student deleted successfully!\n")
else:
    print("Student not found!\n")


# READ ALL AGAIN
print("----- All Students After Update & Delete -----")

for student in repository.get_all_students():
    student.show_info()
    print()