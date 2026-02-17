import requests

# Test courses page has nav buttons
r1 = requests.get('http://127.0.0.1:8000/courses/')
has_assignments_btn = 'goToAssignments' in r1.text
has_student_btn = 'goToStudentDetails' in r1.text
print(f'Courses page has Assignments btn: {has_assignments_btn}')
print(f'Courses page has Student Details btn: {has_student_btn}')

# Test assignments page has nav buttons
r2 = requests.get('http://127.0.0.1:8000/assignments/')
has_courses_btn = 'goBack' in r2.text or 'Back to Courses' in r2.text
has_student_in_assign = 'goToStudentDetails' in r2.text
print(f'\nAssignments page has Back to Courses btn: {has_courses_btn}')
print(f'Assignments page has Student Details btn: {has_student_in_assign}')

# Test student-details page has nav buttons
r3 = requests.get('http://127.0.0.1:8000/student-details.html')
has_courses_in_student = 'goToCourses' in r3.text
has_assignments_in_student = 'goToAssignments' in r3.text
print(f'\nStudent Details page has Back to Courses btn: {has_courses_in_student}')
print(f'Student Details page has Assignments btn: {has_assignments_in_student}')

# Check for student details content
has_profile = 'Student Profile' in r3.text
has_stats = 'Enrolled Courses' in r3.text
print(f'\nStudent Details has profile header: {has_profile}')
print(f'Student Details has stats: {has_stats}')
