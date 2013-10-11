from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class SimpleUserCreation(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder': 'Company Email Address'}))
	full_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder': 'Full Name'}))
	username = forms.CharField(required=False, widget=forms.widgets.HiddenInput())
	first_name = forms.CharField(required=False, widget=forms.widgets.HiddenInput())
	last_name = forms.CharField(required=False, widget=forms.widgets.HiddenInput())
	role = forms.ChoiceField(
		widget=forms.Select(attrs={
            'class':'form-control'
        }),
        choices=(
            ("Team Leader", "Team Leader"),
            ("Team Member", "Team Member"),
        ),
        help_text=u'Select your Role :',
        initial='Team Member',
    )
	password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))
	password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class':'form-control','placeholder': 'Password Confirmation'}))
	company_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder': 'Company Name'}))
	
	class Meta:
		model = User
		fields = ["full_name","company_name","email","role","password1","password2"]

class SimpleAuthForm(AuthenticationForm):
	email = forms.EmailField(widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder': 'Email Address'}))
	company_name = forms.ChoiceField(widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder': 'Company Name'}))
	username = forms.CharField(required=False, widget=forms.widgets.HiddenInput())	
	password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))
	
	class Meta:
		model = User
		fields = ["email","company_name","username","password"]

	def __init__(self, *args, **kwargs):
	    super(SimpleAuthForm, self).__init__(*args, **kwargs)
	    self.fields.keyOrder = [
	        'email',
	        'username',
	        'password']

	