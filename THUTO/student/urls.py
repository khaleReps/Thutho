from django.urls import path
from . import views 


urlpatterns = [   
    path('student-billing-history/', views.billing_history, name='student-billing-history'),
    path('student-billing/', views.billing, name='student-billing'),
    path('student-billing-invoice/', views.billing_invoice, name='student-billing-invoice'),
    path('student-billing-payment/', views.billing_payment, name='student-billing-payment'),
    path('student-billing-upgrade/', views.billing_upgrade, name='student-billing-upgrade'),
    path('student-dashboard/', views.dashboard, name='student-dashboard'),
    path('student-discussion/', views.discussion, name='student-discussion'),
    path('student-discussions-ask/', views.discussions_ask, name='student-discussions-ask'),
    path('student-discussions/', views.discussions, name='student-discussions'),
    path('student-edit_account/', views.edit_account, name='student-edit-account'),
    path('student-edit_account-notifications/', views.edit_account_notifications, name='student-edit-account-notifications'),
    path('student-edit_account-password/', views.edit_account_password, name='student-edit-account-password'),
    path('student-edit_account-profile/', views.edit_account_profile, name='student-edit-account-profile'),
    path('student-my-courses/', views.my_courses, name='student-my-courses'),
    path('student-path-assessment/', views.path_assessment, name='student-path-assessment'),
    path('student-path-assessment-result/', views.path_assessment_result, name='student-path-assessment-result'),
    path('student-profile/', views.profile, name='student-profile'),
    path('student-quiz-result-details/', views.quiz_result_details, name='student-quiz-result-details'),
    path('student-quiz-results/', views.quiz_results, name='student-quiz-results'),
    path('student-take-course/', views.take_course, name='student-take-course'),
    path('student-take-lesson/', views.take_lesson, name='student-take-lesson'),
    path('student-take-quiz/', views.take_quiz, name='student-take-quiz'),


]