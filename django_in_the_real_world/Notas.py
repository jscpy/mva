#-------------------------------------------------------------------------
# ADD USER FORM IN DJANGO

from django.contrib.auth.models import User

new_user=User.objects.create_user(self.cleaned_data['username'], 
								  self.cleaned_data['email'], 
								  self.cleaned_data['password1'])

new_user.first_name = self.cleaned_data['first_name']
new_user.last_name = self.cleaned_data['last_name']
new_user.save()

#-------------------------------------------------------------------------
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.

#-------------------------------------------------------------------------
class UserForm(django.forms.ModelForm):
    class Meta:
        model = User  

class UserProfileForm(django.forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        
#-------------------------------------------------------------------------
# Limiting access to logged-in users

from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # ...

from django.shortcuts import render

def my_view(request):
    if not request.user.is_authenticated():
        return render(request, 'myapp/login_error.html')
    # ...

#-------------------------------------------------------------------------
#The login_required decorator

from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
	...

#-------------------------------------------------------------------------
#forms.py
class UserCreationForm(forms.ModelForm):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',max_length=30,label='Username')
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Repeat Password")

    class Meta:
        models = User
        fields = ('username','email','password1','password2')

#views.py
from myapp.register.forms import UserCreationForm
class CreateUser(FormView):
     template_name = 'registration/registration_form.html'
     success:url = '/'
     form_class = UserCreationForm
    def is_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password1'])
        #user.save()
        return super(CreateUser, self).form_valid(form)