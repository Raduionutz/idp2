from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from . import forms

def index(request):
    return render(request, 'store/index.html')
@login_required
def add(request):
    return render(request, 'store/add.html')

def logout_adm(request):

    logout(request)

    return HttpResponseRedirect(reverse('store:index_adm'))

def login_adm(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('store:index_adm'))
            else:
                return HttpResponse('Your account is not active.')
        else:
            return HttpResponse('Invalid login details supplied.')

    else:
        return render(request, 'store/login.html', {})

def register(request):
    registered = False

    if request.method == 'POST':

        user_form = forms.RegForm(data=request.POST)

        if user_form.is_valid() and user_form.cleaned_data['email'] == 'secret@secret.secret':

            # Save User Form to Database
            user = user_form.save()
            #
            # # Hash the password
            user.set_password(user.password)
            # # Update with Hashed password
            user.save()

            registered = True

        else:
            # One of the forms was invalid if this gets called.
            print(user_form.errors)

    else:
        user_form = forms.RegForm()

    return render(
        request,
        'store/register.html',
        {
            'user_form': user_form,
            'registered': registered,
        }
    )
