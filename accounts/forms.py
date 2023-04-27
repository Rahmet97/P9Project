from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password'
    }))


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)