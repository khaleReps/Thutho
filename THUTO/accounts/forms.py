from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import Order


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	gender = forms.ChoiceField(choices=GENDER_CHOICES)

	ROLE_CHOICES = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
	occupation = forms.ChoiceField(choices=ROLE_CHOICES)

	# first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	
	# student_number = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


	class Meta:
		model = User
		fields = ['occupation', 'username', 'gender','email', 'password1', 'password2']

