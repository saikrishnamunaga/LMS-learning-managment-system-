import requests

# Test assignment detail page
r1 = requests.get('http://127.0.0.1:8000/assignment-detail.html')
print(f'Assignment detail page: {r1.status_code}')
print(f'Has submission form: {"submissionForm" in r1.text}')
print(f'Has task code display: {"task-code" in r1.text}')
print(f'Has submit button: {"Submit Assignment" in r1.text}')

# Test assignments list page has correct links
r2 = requests.get('http://127.0.0.1:8000/assignments/')
print(f'\nAssignments list page: {r2.status_code}')
print(f'Has View & Submit links: {"View & Submit" in r2.text}')
print(f'Has assignment-detail links: {"assignment-detail.html" in r2.text}')

# Get all assignments from API
r3 = requests.post('http://127.0.0.1:8000/api/token/', 
    json={'username':'testuser','password':'testpass123'})
if r3.status_code == 200:
    token = r3.json()['access']
    r4 = requests.get('http://127.0.0.1:8000/api/courses/assignments/',
        headers={'Authorization': f'Bearer {token}'})
    print(f'\nAPI assignments: {r4.status_code}')
    print(f'Number of assignments: {len(r4.json())}')
    for a in r4.json()[:3]:
        print(f'  - {a["title"]}')
