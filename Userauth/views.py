import sweetify
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import json

import shared.sharedfile
from Userauth.forms.form import SignupForm, VerifyUserForm, LoginForm
from Userauth.models import Users


class Home(View):
    def get(self, request):
        signupform = SignupForm()
        verifyUserForm = VerifyUserForm()
        loginForm = LoginForm()
        context = {'signupform': signupform, 'verifyUserForm': verifyUserForm, 'loginform': loginForm}
        return render(request, 'home.html', context=context)


class signInView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        if request.method == 'POST':
            signupform = SignupForm(json.loads(request.body))
            if signupform.is_valid():
                data = signupform.cleaned_data
                if User.objects.filter(username=data['username']):
                    return JsonResponse({'status': 401, 'message': 'User Already Exists'})
                user = User()
                user.username = data['username']
                user.email = data['username']
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.set_password(data['password'])
                user.save()
                password = make_password(data['password'])
                random_otp = shared.sharedfile.generate_otp(5)
                userauth_obj = Users.objects.create(
                    username_id=user.id,
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['username'],
                    password=password,
                    is_active=False,
                    is_verified=False,
                    otp=random_otp
                )
                email_sent = shared.sharedfile.send_otp_mail(userauth_obj)
                if email_sent:
                    return JsonResponse({'status': 'success', 'message': 'OTP sent to your email'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Something went wrong, Try again later'})
            else:
                context = {'signupform': signupform, 'status': 'validationFailed'}
                return render(request, '_partial/_signupForm.html', context=context)


class loginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        if request.method == 'POST':
            loginForm = LoginForm(json.loads(request.body))
            if loginForm.is_valid():
                data = loginForm.cleaned_data
                try:
                    user_obj = get_object_or_404(Users, email=data['login_username'])
                except:
                    return JsonResponse({'status': 'error', 'message': 'User Not Found'})
                if user_obj.is_active == True:
                    user = authenticate(request, username=data['login_username'], password=data['login_password'])
                    if user is not None:
                        login(request, user)
                        print(user_obj)
                        return JsonResponse({'statusCode': 200, 'message': {'email':user_obj.email,'access_token': user_obj.access_token}})
                        # return JsonResponse({'status': 'success', 'message': 'Login Successful'})
                    else:
                        return JsonResponse({'status': 401, 'message': 'Invalid Credentials'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'User is not active'})

            else:
                return JsonResponse({'status': 401, 'message': 'Invalid Credentials'})
                # context = {'loginform': loginForm, 'status': 'validationFailed'}
                # return render(request, '_partial/_loginForm.html', context=context)


class verifyToken(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        print(json.loads(request.body))
        token = json.loads(request.body)['confirmation_code']
        if token:
            userauth_obj = Users.objects.filter(otp=token).first()
            if userauth_obj:
                userauth_obj.is_active = True
                userauth_obj.is_verified = True
                userauth_obj.save()
                return JsonResponse({'status':200,'message':'user verified'})
                # sweetify.success(request, 'Account Verified Successfully')
                # return HttpResponseRedirect('/')
            else:
                return JsonResponse({'status': 400, 'message': 'Wrong Otp'})
                # sweetify.error(request, 'Invalid OTP')
                # return HttpResponseRedirect('/')


# class moviesView(View):
#     def get(self, request):
#         print(request.user)
#         if request.user.is_authenticated:
#             movies = Movies.objects.all()
#             context = {'user': request.user}
#             return render(request, 'movies.html', context=context)
#         else:
#             return HttpResponseRedirect('/')


class logoutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse({'status': 'success', 'message': 'Logout Successful'})
