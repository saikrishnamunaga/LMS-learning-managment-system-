import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()
instructor = User.objects.first()

courses_data = [
    ("Python Basics", "Learn Python programming fundamentals"),
    ("Web Development", "Master HTML, CSS, and JavaScript"),
    ("Data Science", "Introduction to pandas, numpy, and matplotlib"),
    ("Machine Learning", "Learn ML algorithms and TensorFlow"),
    ("Django Framework", "Build web applications with Django"),
    ("Advanced Python", "Decorators, generators, and async programming"),
    ("Database Design", "SQL and relational database management"),
    ("API Development", "RESTful API design and implementation"),
    ("Cloud Computing", "AWS and cloud infrastructure basics"),
    ("DevOps Fundamentals", "Docker, Kubernetes, and CI/CD pipelines"),
]

for title, description in courses_data:
    if not Course.objects.filter(title=title).exists():
        Course.objects.create(
            title=title,
            description=description,
            instructor=instructor
        )
        print(f"Created: {title}")

print(f"\nTotal courses: {Course.objects.count()}")
