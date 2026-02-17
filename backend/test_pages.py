import requests

pages = {
    'assignments/': 'Assignments page',
    'student-details.html': 'Student details page',
    'courses/': 'Courses page'
}

for page, desc in pages.items():
    try:
        r = requests.get(f'http://127.0.0.1:8000/{page}')
        print(f'{desc}: {r.status_code}')
    except Exception as e:
        print(f'{desc}: ERROR - {str(e)}')
