import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()
instructor = User.objects.first()

courses_data = [
    ("Python Basics", "Learn Python programming fundamentals", "https://www.youtube.com/watch?v=_uQrJ0TkZlc"),
    ("Web Development", "Master HTML, CSS, and JavaScript", "https://www.youtube.com/watch?v=UB1O30fR-EE"),
    ("Data Science", "Introduction to pandas, numpy, and matplotlib", "https://www.youtube.com/watch?v=ua-CiDNNj30"),
    ("Machine Learning", "Learn ML algorithms and TensorFlow", "https://www.youtube.com/watch?v=i_LwzRVP7bg"),
    ("Django Framework", "Build web applications with Django", "https://www.youtube.com/watch?v=F5mRW0jo-U4"),
    ("Advanced Python", "Decorators, generators, and async programming", "https://www.youtube.com/watch?v=rfscVS0vtbw"),
    ("Database Design", "SQL and relational database management", "https://www.youtube.com/watch?v=HXV3zeQKqGY"),
    ("API Development", "RESTful API design and implementation", "https://www.youtube.com/watch?v=pXyZ6t3F-e4"),
    ("Cloud Computing", "AWS and cloud infrastructure basics", "https://www.youtube.com/watch?v=SOTamWNgDKc"),
    ("DevOps Fundamentals", "Docker, Kubernetes, and CI/CD pipelines", "https://www.youtube.com/watch?v=fqMOX6JJhGo"),
]

for title, description, youtube_link in courses_data:
    course, created = Course.objects.get_or_create(
        title=title,
        defaults={
            'description': description,
            'instructor': instructor,
            'youtube_link': youtube_link
        }
    )
    if created:
        print(f"Created: {title}")
    else:
        # Update the youtube_link if course already exists
        course.youtube_link = youtube_link
        course.save()
        print(f"Updated: {title}")

print(f"\nTotal courses: {Course.objects.count()}")
