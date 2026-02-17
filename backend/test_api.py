import requests

# Login
r1 = requests.post('http://127.0.0.1:8000/api/token/', 
    json={'username':'testuser','password':'testpass123'})
token = r1.json()['access']

# Get courses
r2 = requests.get('http://127.0.0.1:8000/api/courses/', 
    headers={'Authorization': f'Bearer {token}'})

print(f'Courses API Status: {r2.status_code}')
print(f'Number of courses: {len(r2.json())}')
for course in r2.json():
    print(f'  - {course["title"]}')
