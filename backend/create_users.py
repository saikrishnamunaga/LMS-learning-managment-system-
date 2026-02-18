import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create instructor/teacher user
if not User.objects.filter(username='teacher').exists():
    teacher = User.objects.create_user(
        username='teacher',
        email='teacher@lms.com',
        password='teacher123',
        role='instructor'
    )
    print(f"Created teacher user: teacher / teacher123")
else:
    print("Teacher user already exists: teacher / teacher123")

# Create student user
if not User.objects.filter(username='student').exists():
    student = User.objects.create_user(
        username='student',
        email='student@lms.com',
        password='student123',
        role='student'
    )
    print(f"Created student user: student / student123")
else:
    print("Student user already exists: student / student123")

# Create admin user
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@lms.com',
        password='admin123'
    )
    print(f"Created admin user: admin / admin123")
else:
    print("Admin user already exists: admin / admin123")

print("\nAll test users created successfully!")
print("You can now login with these credentials:")
print("Teacher (Instructor): username: teacher, password: teacher123")
print("Student: username: student, password: student123")
print("Admin: username: admin, password: admin123")
