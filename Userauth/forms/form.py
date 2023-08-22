from django import forms
from django.core.exceptions import ValidationError

from Userauth.models import Users


class SignupForm(forms.Form):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'password']

    username = forms.EmailField(label='Username', max_length=100, required=True,
                                widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True,
                                       label='Confirm Password', max_length=100)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters long")
        if username.isdigit():
            raise forms.ValidationError("Username must not be a number")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 4:
            raise forms.ValidationError("First name must be at least 4 characters long")
        if first_name.isdigit():
            raise forms.ValidationError("First Name must not be a number")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 4:
            raise forms.ValidationError("Last name must be at least 4 characters long")
        if last_name.isdigit():
            raise forms.ValidationError("Last Name must not be a number")
        return last_name

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        return password

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class VerifyUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    otp = forms.CharField(label='OTP', max_length=100, required=True)


class LoginForm(forms.Form):
    login_username = forms.CharField(label='Username', max_length=100, required=True,
                                     widget=forms.EmailInput(attrs={'class': 'form-control'}))
    login_password = forms.CharField(label='Password', max_length=100, required=True,
                                     widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_login_username(self):
        username = self.cleaned_data.get('login_username')
        if len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters long")
        if username.isdigit():
            raise forms.ValidationError("Username must not be a number")
        return username

    def clean_login_password(self):
        password = self.cleaned_data.get('login_password')
        if len(password) < 4:
            raise forms.ValidationError("Password must be at least 4 characters long")
        return password
