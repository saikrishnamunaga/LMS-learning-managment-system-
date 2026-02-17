import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from courses.models import Course, Assignment

User = get_user_model()

# Get first instructor
instructor = User.objects.first()

# Get courses
courses = Course.objects.all()[:3]

assignments_data = [
    {
        "course": courses[0] if courses else None,
        "title": "Python Variables and Data Types",
        "description": "Create a program that handles different data types",
        "due_date": "2026-02-24 23:59:59",
        "task": """Write a Python program that:
1. Creates variables of different types (int, str, float, bool)
2. Prints each variable with its type
3. Performs type conversion and prints results

Example output:
x = 10 (type: <class 'int'>)
y = "Hello" (type: <class 'str'>)
z = 3.14 (type: <class 'float'>)
Converted: 10.0
"""
    },
    {
        "course": courses[0] if courses else None,
        "title": "List and Dictionary Operations",
        "description": "Manipulate lists and dictionaries in Python",
        "due_date": "2026-02-26 23:59:59",
        "task": """Write a Python program that:
1. Creates a list of 5 numbers
2. Adds, removes, and sorts elements
3. Creates a dictionary with student information
4. Accesses and modifies dictionary values

Tasks:
- List operations: append, remove, sort
- Dictionary operations: get, update, keys(), values()
- Print all operations with results
"""
    },
    {
        "course": courses[1] if len(courses) > 1 else None,
        "title": "HTML Form Creation",
        "description": "Create a functional HTML form",
        "due_date": "2026-02-25 23:59:59",
        "task": """Create an HTML form with:
1. Text input for name
2. Email input field
3. Password input field
4. Select dropdown for country
5. Checkbox for terms agreement
6. Submit and Reset buttons

Requirements:
- Use proper HTML5 form elements
- Add labels for each field
- Include form validation attributes
- Style with CSS
"""
    },
    {
        "course": courses[1] if len(courses) > 1 else None,
        "title": "JavaScript Function Practice",
        "description": "Write JavaScript functions for common tasks",
        "due_date": "2026-02-27 23:59:59",
        "task": """Write JavaScript functions for:
1. calculateSum(a, b) - returns sum of two numbers
2. reverseString(str) - returns reversed string
3. findMax(arr) - returns maximum value in array
4. isPalindrome(str) - checks if string is palindrome
5. countVowels(str) - counts vowels in string

Test each function with sample inputs
"""
    },
    {
        "course": courses[2] if len(courses) > 2 else None,
        "title": "SQL Database Queries",
        "description": "Write SQL queries to retrieve and modify data",
        "due_date": "2026-02-28 23:59:59",
        "task": """Write SQL queries for:
1. SELECT all students from database
2. SELECT students ordered by name
3. SELECT students with age > 20
4. COUNT total number of students
5. JOIN students with courses table

Sample queries provided:
-- Get all records
SELECT * FROM students;

-- Filter by age
SELECT * FROM students WHERE age > 20;

-- Order results
SELECT * FROM students ORDER BY name;
"""
    },
    {
        "course": courses[0] if courses else None,
        "title": "File Handling in Python",
        "description": "Read, write, and manipulate files",
        "due_date": "2026-03-01 23:59:59",
        "task": """Create a program that:
1. Writes student names to a file
2. Reads the file and counts lines
3. Searches for a specific name
4. Appends new data to the file
5. Displays file contents

Operations required:
- Open file in write mode
- Open file in read mode
- Open file in append mode
- Handle file exceptions
"""
    }
]

# Create assignments
for data in assignments_data:
    if data['course']:
        if not Assignment.objects.filter(title=data['title']).exists():
            Assignment.objects.create(
                title=data['title'],
                description=data['description'],
                due_date=data['due_date'],
                course=data['course']
            )
            print(f"Created: {data['title']}")

print(f"\nTotal assignments: {Assignment.objects.count()}")
