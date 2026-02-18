# Mini LMS - Learning Management System

A lightweight Learning Management System built with Django and Django REST Framework. Mini LMS allows instructors to create and manage courses, assignments, and lessons while enabling students to enroll in courses, view content, and submit assignments.

## Features

### User Roles
- **Admin**: Full system access administration
- **Instructor**: Create and manage courses, lessons, and assignments
- **Student**: Enroll in courses, view content, submit assignments

### Core Functionality
- User authentication with JWT (JSON Web Tokens)
- Course management (create, view, edit courses)
- Lesson content management
- Assignment creation and due date tracking
- Student submission system
- RESTful API for all operations

## Tech Stack

- **Backend**: Django 6.0
- **API Framework**: Django REST Framework
- **Authentication**: JWT (rest_framework_simplejwt)
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **CORS**: django-cors-headers

## Project Structure

```
mini_lms/
├── backend/
│   ├── accounts/           # User authentication app
│   │   ├── models.py       # Custom User model with roles
│   │   ├── serializers.py # DRF serializers
│   │   ├── views.py        # API views
│   │   └── urls.py         # URL routing
│   ├── courses/            # Course management app
│   │   ├── models.py       # Course, Lesson, Assignment, Submission models
│   │   ├── serializers.py  # DRF serializers
│   │   ├── views.py        # API views
│   │   └── urls.py         # URL routing
│   ├── frontend/           # Frontend HTML files
│   │   ├── index.html      # Home/Login page
│   │   ├── signup.html     # User registration
│   │   ├── courses.html    # Course listing
│   │   ├── course-detail.html # Course details
│   │   ├── assignments.html    # Assignment listing
│   │   ├── assignment-detail.html # Assignment details
│   │   ├── student-details.html  # Student profile
│   │   └── style.css      # Styling
│   ├── backend/            # Django project settings
│   │   ├── settings.py    # Project configuration
│   │   └── urls.py        # Main URL routing
│   ├── manage.py           # Django management script
│   └── db.sqlite3         # SQLite database
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 6.0+

### Setup Steps

1. **Navigate to the backend directory:**
   
```
bash
   cd mini_lms/backend
   
```

2. **Install dependencies:**
   
```
bash
   pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
   
```

3. **Run migrations:**
   
```
bash
   python manage.py migrate
   
```

4. **Create a superuser (optional):**
   
```
bash
   python manage.py createsuperuser
   
```

5. **Run the development server:**
   
```
bash
   python manage.py runserver
   
```

6. **Access the application:**
   - Frontend: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API: http://127.0.0.1:8000/api/

## API Endpoints

### Authentication
- `POST /api/register/` - Register a new user
- `POST /api/login/` - Login and get JWT tokens
- `POST /api/token/refresh/` - Refresh JWT token

### Courses
- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create a new course (Instructor/Admin)
- `GET /api/courses/<id>/` - Get course details
- `PUT /api/courses/<id>/` - Update course (Instructor/Admin)
- `DELETE /api/courses/<id>/` - Delete course (Instructor/Admin)

### Lessons
- `GET /api/courses/<course_id>/lessons/` - List lessons for a course
- `POST /api/courses/<course_id>/lessons/` - Create lesson (Instructor/Admin)

### Assignments
- `GET /api/courses/<course_id>/assignments/` - List assignments
- `POST /api/courses/<course_id>/assignments/` - Create assignment (Instructor/Admin)
- `GET /api/assignments/<id>/` - Get assignment details

### Submissions
- `GET /api/assignments/<assignment_id>/submissions/` - List submissions
- `POST /api/assignments/<assignment_id>/submissions/` - Submit assignment (Student)

## User Roles & Permissions

| Feature | Admin | Instructor | Student |
|---------|-------|------------|---------|
| View Courses | ✓ | ✓ | ✓ |
| Create Courses | ✓ | ✓ | ✗ |
| Edit Courses | ✓ | ✓ (own) | ✗ |
| Delete Courses | ✓ | ✗ | ✗ |
| Create Assignments | ✓ | ✓ (own) | ✗ |
| Submit Assignments | ✓ | ✗ | ✓ |
| View All Submissions | ✓ | ✓ (own) | ✗ (own) |

## Database Models

### User
- username, email, password
- role (admin, instructor, student)

### Course
- title, description
- instructor (ForeignKey to User)

### Lesson
- title, content
- course (ForeignKey to Course)

### Assignment
- title, description, due_date
- course (ForeignKey to Course)

### Submission
- assignment (ForeignKey to Assignment)
- student (ForeignKey to User)
- content, submitted_at

## Testing

Run tests with:
```
bash
python manage.py test
```

Test files included:
- `test_api.py` - API endpoint tests
- `test_assignments.py` - Assignment functionality tests
- `test_course_detail.py` - Course detail page tests
- `test_navigation.py` - Navigation tests
- `test_pages.py` - Page rendering tests

## Development Utilities

### Create Sample Courses
```
bash
python create_courses.py
```

### Create Sample Assignments
```
bash
python create_assignments.py
```

## Frontend Pages

| Page | Description |
|------|-------------|
| index.html | Landing page with login form |
| signup.html | User registration form |
| courses.html | List of all available courses |
| course-detail.html | Course details with lessons and assignments |
| assignments.html | List of assignments |
| assignment-detail.html | Assignment details and submission form |
| student-details.html | Student profile and enrolled courses |

## License

This project is for educational purposes.
