"""Course domain model."""

from dataclasses import dataclass


@dataclass
class Course:
    """Course model."""

    course_id: int
    name: str
    teacher_id: int | None = None
