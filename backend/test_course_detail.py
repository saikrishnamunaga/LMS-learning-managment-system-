import requests

# Login
r1 = requests.post('http://127.0.0.1:8000/api/token/', 
    json={'username':'testuser','password':'testpass123'})
token = r1.json()['access']
print(f'Login: {r1.status_code}')

# Get courses
r2 = requests.get('http://127.0.0.1:8000/api/courses/', 
    headers={'Authorization': f'Bearer {token}'})
print(f'Get courses: {r2.status_code}')

courses = r2.json()
if courses:
    course = courses[0]
    print(f'\nFirst course:')
    print(f'  ID: {course["id"]}')
    print(f'  Title: {course["title"]}')
    print(f'\nTest URL would be: /course-detail.html?id={course["id"]}')
