"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from rest_framework_simplejwt.views import TokenObtainPairView
import os

def serve_index(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(base_dir, 'frontend', 'index.html')
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        response = HttpResponse(content, content_type='text/html')
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    except Exception as e:
        return HttpResponse(f'Error loading index: {str(e)}', status=500)

@never_cache
def serve_static_file(request, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'frontend', filename)
    if file_path.endswith('.css'):
        content_type = 'text/css'
    elif file_path.endswith('.html'):
        content_type = 'text/html'
    elif file_path.endswith('.js'):
        content_type = 'application/javascript'
    else:
        content_type = 'text/plain'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        response = HttpResponse(content, content_type=content_type)
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    except FileNotFoundError:
        return HttpResponse('Not Found', status=404)
    except Exception as e:
        return HttpResponse(f'Error loading file: {str(e)}', status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/courses/', include('courses.urls')),
    path('', serve_index),
    path('signup', serve_static_file, {'filename': 'signup.html'}),
    path('courses/', serve_static_file, {'filename': 'courses.html'}),
    path('course-detail.html', serve_static_file, {'filename': 'course-detail.html'}),
    path('assignments/', serve_static_file, {'filename': 'assignments.html'}),
    path('assignment-detail.html', serve_static_file, {'filename': 'assignment-detail.html'}),
    path('student-details.html', serve_static_file, {'filename': 'student-details.html'}),
    path('style.css', serve_static_file, {'filename': 'style.css'}),
]
