from django.urls import path
from . import views


urlpatterns = [
	path('instructor-courses/', views.courses, name='instructor-courses'),
    path('instructor-dashboard/', views.dashboard, name='instructor-dashboard'),
    path('instructor-earnings/', views.earnings, name='instructor-earnings'),
    path('instructor-edit_course/', views.edit_course, name='instructor-edit-course'),
    path('instructor-edit_quiz/', views.edit_quiz, name='instructor-edit-quiz'),
    path('instructor-profile/', views.profile, name='instructor-profile'),
    path('instructor-quizzes/', views.quizzes, name='instructor-quizzes'),
    path('instructor-statement/', views.statement, name='instructor-statement'),

    path('lesson', views.lesson, name='lesson'),
    path('course', views.course, name='course'),
    path('path', views.path, name='path'),
    path('paths', views.paths, name='paths'),

    path('pricing', views.pricing, name='instructor-pricing'),
    path('invoice', views.invoice, name='invoice'),



]