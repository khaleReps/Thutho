from django.shortcuts import render, redirect 

# Create your views here.

def courses(request):
    context = {}
    return render(request, 'instructor/instructor_courses.html', context)
def dashboard(request):
    context = {}
    return render(request, 'instructor/instructor_dashboard.html', context)
def earnings(request):
    context = {}
    return render(request, 'instructor/instructor_earnings.html', context)
def edit_course(request):
    context = {}
    return render(request, 'instructor/instructor_edit_course.html', context)
def edit_quiz(request):
    context = {}
    return render(request, 'instructor/instructor_edit_quiz.html', context)
def profile(request):
    context = {}
    return render(request, 'instructor/instructor_profile.html', context)
def quizzes(request):
    context = {}
    return render(request, 'instructor/instructor_quizzes.html', context)
def statement(request):
    context = {}
    return render(request, 'instructor/instructor_statement.html', context)


def lesson(request):
	context = {}
	return render(request, 'instructor/lesson.html', context)

def course(request):
	context = {}
	return render(request, 'instructor/course.html', context)

def paths(request):
	context = {}
	return render(request, 'instructor/paths.html', context)


def path(request):
	context = {}
	return render(request, 'instructor/path.html', context)


def pricing(request):
	context = {}
	return render(request, 'instructor/pricing.html.', context)


def invoice(request):
	context = {}
	return render(request, 'instructor/invoice.html.', context)

