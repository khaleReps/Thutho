from django.shortcuts import render, redirect 
# from django.http import HttpResponse
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth import authenticate, login, logout

# from django.contrib import messages

# from django.contrib.auth.decorators import login_required

# Create your views here.
def billing_history(request):
    context = {}
    return render(request, 'student/student-billing_history.html',context)

def billing(request):
    context = {}
    return render(request, 'student/student-billing.html',context)

def billing_invoice(request):
    context = {}
    return render(request, 'student/student-billing_invoice.html',context)

def billing_payment(request):
    context = {}
    return render(request, 'student/student-billing_payment.html',context)

def billing_upgrade(request):
    context = {}
    return render(request, 'student/student-billing_upgrade.html',context)

def dashboard(request):
    context = {}
    return render(request, 'student/student-dashboard.html',context)

def discussion(request):
    context = {}
    return render(request, 'student/student-discussion.html',context)

def discussions_ask(request):
    context = {}
    return render(request, 'student/student-discussions_ask.html',context)

def discussions(request):
    context = {}
    return render(request, 'student/student-discussions.html',context)

def edit_account(request):
    context = {}
    return render(request, 'student/student-edit_account.html',context)

def edit_account_notifications(request):
    context = {}
    return render(request, 'student/student-edit_account_notifications.html',context)

def edit_account_password(request):
    context = {}
    return render(request, 'student/student-edit_account_password.html',context)

def edit_account_profile(request):
    context = {}
    return render(request, 'student/student-edit_account_profile.html',context)

def my_courses(request):
    context = {}
    return render(request, 'student/student-my_courses.html',context)

def path_assessment(request):
    context = {}
    return render(request, 'student/student-path_assessment.html',context)

def path_assessment_result(request):
    context = {}
    return render(request, 'student/student-path_assessment_result.html',context)

def profile(request):
    context = {}
    return render(request, 'student/student-profile.html',context)

def quiz_result_details(request):
    context = {}
    return render(request, 'student/student-quiz_result_details.html',context)

def quiz_results(request):
    context = {}
    return render(request, 'student/student-quiz_results.html',context)

def take_course(request):
    context = {}
    return render(request, 'student/student-take_course.html',context)

def take_lesson(request):
    context = {}
    return render(request, 'student/student-take_lesson.html',context)

def take_quiz(request):
    context = {}
    return render(request, 'student/student-take_quiz.html',context)
