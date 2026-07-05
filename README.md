# School Management System

A simple object-oriented **School Management System** built in Python. It models a school with classrooms, students, teachers, and subjects — and simulates a semester final exam, calculating each student's grades and final GPA.

## Features

- Create a school with multiple classrooms
- Admit students into specific classrooms
- Assign teachers to subjects
- Assign subjects to classrooms
- Simulate a semester final exam (random marks generated per subject)
- Automatic grade calculation per subject (A+, A, A-, B, C, F)
- Automatic GPA calculation and final grade per student
- Clean printable report of all classrooms, students, subjects, and results

## Project Structure

| File | Description |
|---|---|
| `main.py` | Entry point — sets up the school, classrooms, students, teachers, and subjects, then runs the exams |
| `school.py` | `School` class — manages classrooms/teachers, grade conversion logic, and the final report (`__repr__`) |
| `classroom.py` | `ClassRoom` class — manages students and subjects within a classroom, triggers exams |
| `person.py` | `Person`, `Teacher`, and `Student` classes — base person model, exam evaluation, and grade/GPA calculation |
| `subject.py` | `Subject` class — represents a subject taught by a teacher, handles exam logic for students |

## How to Run

Make sure you have Python 3 installed, then from the project folder run:

```bash
python main.py
```

## Sample Output

```
Eight
Nine
Ten
All Students: 
---EIGHT--Classroom Students 
Rahi
---NINE--Classroom Students 
Mahi
---TEN--Classroom Students 
Fahi
Bahi
...
Rahi Bangla 71 A
Rahi Physics 88 A+
Rahi Chemistry 79 A
Rahi Final Grade: A with GPA= 4.33
```

Note: exam marks are generated randomly each run, so grades/GPA will vary between runs.

## Concepts Demonstrated

- **Object-Oriented Programming (OOP)**: classes, objects, and relationships between them (School → Classroom → Student/Subject)
- **Inheritance**: `Teacher` and `Student` both inherit from a shared `Person` base class
- **Encapsulation**: use of `@property` and `@id.setter` to control access to a student's ID
- **Static methods**: grade conversion and GPA logic implemented as `@staticmethod` in `School`
- **Custom string representation**: `__repr__` overridden in `School` to produce a full formatted report

## Author

Built as a learning project to practice Python OOP concepts.
