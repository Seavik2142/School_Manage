
import pytest
from models.student import Student
from repositories.student_repository import StudentRepository
from services.student_service import StudentService


def test_register_student():
    # Arrange
    repository = StudentRepository()
    service = StudentService(repository)

    student = Student(
        "S001",
        "Seavik",
        "seavik@gmail.com",
        "password123",
        "Computer Science"
    )

    # Act
    service.register_student(student)

    # Assert
    saved_student = repository.find_student("S001")

    assert saved_student is not None
    assert saved_student == student
    assert saved_student.email == "seavik@gmail.com"


def test_register_student_invalid_email():
    # Arrange
    repository = StudentRepository()
    service = StudentService(repository)

    student = Student(
        "S002",
        "Dara",
        "invalid-email",
        "password123",
        "Computer Science"
    )

    # Act & Assert
    with pytest.raises(ValueError):
        service.register_student(student)
