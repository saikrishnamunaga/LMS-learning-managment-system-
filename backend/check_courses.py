import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from courses.models import Course

courses = Course.objects.all()
print(f'Total courses: {courses.count()}')
for i, course in enumerate(courses, 1):
    print(f'{i}. {course.title}')
