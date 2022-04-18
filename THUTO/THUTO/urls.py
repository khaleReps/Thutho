"""THUTO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class_based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),

    # account
    path('invoice/', include('accounts.urls')),
    path('pricing/', include('accounts.urls')),  
    # path('pricing/', include('accounts.urls')), 
    # path('pricing/', include('accounts.urls')), 
    # path('pricing/', include('accounts.urls')),       


    # Student
    path('student-billing-history/', include('student.urls')),
    path('student-billing/', include('student.urls')),
    path('student-billing-invoice/', include('student.urls')),
    path('student-billing-payment/', include('student.urls')),
    path('student-billing-upgrade/', include('student.urls')),
    path('student-dashboard/', include('student.urls')),
    path('student-discussion/', include('student.urls')),
    path('student-discussions-ask/', include('student.urls')),
    path('student-discussions/', include('student.urls')),
    path('student-edit-account/', include('student.urls')),
    path('student-edit-account-notifications/', include('student.urls')),
    path('student-edit-account-password/', include('student.urls')),
    path('student-edit-account-profile/', include('student.urls')),
    path('student-my-courses/', include('student.urls')),
    path('student-path-assessment/', include('student.urls')),
    path('student-path-assessment-result/', include('student.urls')),
    path('student-profile/', include('student.urls')),
    path('student-quiz-result-details/', include('student.urls')),
    path('student-quiz-results/', include('student.urls')),
    path('student-take-course/', include('student.urls')),
    path('student-take-lesson/', include('student.urls')),
    path('student-take-quiz/', include('student.urls')),

    # instructor.urls
    # path('blog/', include('blog.urls')),
    path('instructor-courses/', include('instructor.urls')),
    path('instructor-dashboard/', include('instructor.urls')),
    path('instructor-earnings/', include('instructor.urls')),
    path('instructor-edit-course/', include('instructor.urls')),
    path('instructor-edit-quiz/', include('instructor.urls')),
    path('instructor-profile/', include('instructor.urls')),
    path('instructor-quizzes/', include('instructor.urls')),
    path('instructor-statement/', include('instructor.urls')),

    path('path/', include('instructor.urls')),
    path('paths/', include('instructor.urls')),    

    # library
    path('library-development/', include('library.urls')),
    path('library-featured/', include('library.urls')),
    path('library-filters-development/', include('library.urls')),
    path('library-filters-development_list/', include('library.urls')),
    path('library-filters/', include('library.urls')),
    path('library-filters_list/', include('library.urls')),
    path('library/', include('library.urls')),

    path('ui-buttons/', include('library.urls')),
    path('ui-charts/', include('library.urls')),
    path('ui-avatars/', include('library.urls')),
    path('ui-forms/', include('library.urls')),
    path('ui-loaders/', include('library.urls')),
    path('ui-tables/', include('library.urls')),
    path('ui-cards/', include('library.urls')),
    path('ui-icons/', include('library.urls')),
    path('ui-tabs/', include('library.urls')),
    path('ui-alerts/', include('library.urls')),
    path('ui-badges/', include('library.urls')),
    path('ui-progress/', include('library.urls')),
    path('ui-pagination/', include('library.urls')),
]







