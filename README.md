# Student Grade Management System

## Overview
A modular Python command-line application for managing student grades. It supports validated CRUD operations, persistent JSON storage, student search, and a simple grade summary.

## Features
- Add a student and grade
- Update an existing grade
- Delete a student
- Display all students
- Search for a student
- View grade distribution
- JSON-based persistent storage
- Input validation and error handling
- Automated unit tests

## Technologies
- Python 3.9+
- Standard Python library
- JSON for local storage
- `unittest` for testing
- Git/GitHub for version control

## Project Structure
```text
student_grade_management_project/
├── main.py
├── cli.py
├── student_manager.py
├── storage.py
├── validators.py
├── reports.py
├── config.py
├── test_student_manager.py
├── data/
│   └── students.json
├── statement.md
├── PROJECT_REPORT.pdf
├── requirements.txt
└── .gitignore
```

## Installation
1. Install Python 3.9 or later.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. No third-party packages are required.

## Run
```bash
python main.py
```

## Test
```bash
python -m unittest -v
```

## Input Rules
- Student names cannot be empty and are limited to 60 characters.
- Valid grades are: A+, A, B+, B, C, D, F.
- Duplicate student names are rejected.
- Updating or deleting a missing student produces an error message.

## Storage
Student records are stored locally in `data/students.json`. The program creates the folder/file automatically when needed.

## Academic Alignment
The project demonstrates problem identification, modular design, CRUD operations, input/output handling, validation, persistence, error handling, testing, documentation, and a structured project architecture as required by the VITyarthi Build Your Own Project manual.

## Repository Submission
The repository should contain the source files, `statement.md`, `README.md`, test file, data folder, and project report PDF.
