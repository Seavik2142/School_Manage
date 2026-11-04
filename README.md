# Python Study Project

This repository is a hands-on Python study project built around a small school-management domain. It is intended for practicing Python fundamentals, object-oriented programming, and basic project organization.

## What You Will Practice

- Python modules and packages
- Classes, inheritance, and polymorphism
- Abstract base classes
- Encapsulation and private attributes
- Class methods and static methods
- Dataclasses and type hints
- Lists, loops, functions, and formatted output
- Separating models, services, repositories, and database code

## Project Structure

```text
.
├── main.py
├── models/
│   ├── course.py
│   ├── student.py
│   ├── teacher.py
│   └── user.py
├── services/
│   ├── auth_service.py
│   ├── student_service.py
│   └── teacher_service.py
├── repositories/
│   ├── student_repository.py
│   └── teacher_repository.py
└── database/
    └── db.py
```

### Directory Responsibilities

- **`models/`**: Defines the application's data objects.
- **`services/`**: Contains business logic such as authentication and user operations.
- **`repositories/`**: Intended for reading and writing application data.
- **`database/`**: Intended for database connection and configuration code.
- **`main.py`**: A simple entry point for trying the models.

## Requirements

- Python 3.10 or newer

No third-party packages are currently required.

## Run the Example

From the project directory, run:

```bash
python main.py
```

On systems where `python` points to Python 2, use:

```bash
python3 main.py
```

The example creates a student and a teacher, displays their information, counts users, verifies a password, and validates an email address.

## Suggested Study Path

### 1. Python Basics

Practice the following before changing the application:

- Variables and built-in types
- Strings and f-strings
- Lists and dictionaries
- `if` statements and loops
- Functions and return values
- Exceptions

### 2. Object-Oriented Python

Use the files in `models/` to study:

- Constructors with `__init__`
- Instance attributes and methods
- Inheritance with `Student` and `Teacher`
- Abstract methods in `User`
- Method overriding with `show_info`
- `__str__`
- `@classmethod` and `@staticmethod`
- Name-mangled private attributes such as `__password`

### 3. Data Modeling

Study [`models/course.py`](models/course.py) and compare a dataclass with regular classes:

- Automatic constructor generation
- Type annotations
- Optional values
- Readable object representations

### 4. Application Organization

Move logic out of `main.py` and implement small functions in `services/`. Then use `repositories/` for data access. Keep each layer focused on one responsibility.

### 5. Persistence and Testing

Good next exercises are:

1. Add an in-memory repository for students and teachers.
2. Implement create, read, update, and delete operations.
3. Add SQLite persistence in `database/`.
4. Validate duplicate IDs and invalid email addresses.
5. Add automated tests with Python's `unittest` module.
6. Add type hints to public functions and methods.

## Example Study Exercises

Try these tasks in order:

1. Add a `phone` field to `User`.
2. Add a `remove_course` method to `Student`.
3. Add a `show_info` implementation for `Course`.
4. Create a `School` class that stores users and courses.
5. Add a menu to `main.py` for creating and listing users.
6. Replace printed results with returned values where appropriate.
7. Store users in SQLite and load them when the program starts.

## Learning Goal

The goal is not only to make the example run, but to understand why the code is divided into models, services, repositories, and database components. Build one small feature at a time, run the program after each change, and write a test for behavior that should not break.
