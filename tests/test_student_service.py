
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

def test_register_student_duplicate_id():
    repository = StudentRepository()
    service = StudentService(repository)

    student1 = Student(
        "S001",
        "Seavik",
        "seavik@gmail.com",
        "password123",
        "Computer Science"
    )
    service.register_student(student1)

    student2 = Student(
        "S001",  # Same ID
        "Dara",
        "dara@gmail.com",  # Valid email
        "password123",
        "Computer Science"
    )

    with pytest.raises(ValueError):
        service.register_student(student2)


def test_update_student():
    repository = StudentRepository()
    service = StudentService(repository)

    student = Student(
        "S001",
        "Seavik",
        "seavik@gmail.com",
        "password123",
        "Computer Scient"
    )

    service.register_student(student)

    service.update_student(
        "S001",
        "Seavik Mao",
        "AI engineer",
    )
    saved_student = service.get_student("S001")

    assert saved_student is not None
    assert saved_student.name == "Seavik Mao"
    assert saved_student.major == "AI engineer"


def test_delete_student():
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

    service.register_student(student)

    # Act
    service.delete_student("S001")

    # Assert
    saved_student = repository.find_student("S001")

    assert saved_student is None
