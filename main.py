
from models.student import Student
from models.teacher import Teacher
from models.user import User


student = Student(
    "S001",
    "Mao Seavik",
    "seavik@example.com",
    "password123",
    "Computer Science"
)

teacher = Teacher(
    "T001",
    "John",
    "john@example.com",
    "password456",
    "IT Department"
)


users = [student, teacher]

for user in users:
    user.show_info()
    print()


User.show_total_users()

print(student)
print(student.verify_password("password123"))
print(User.is_valid_email("seavik@example.com"))
