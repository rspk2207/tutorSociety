from django import forms
# from django
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30,required=True,min_length=3)
    password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=8)
    re_password = forms.CharField(widget=forms.PasswordInput,required=True)
    first_name = forms.CharField(max_length=30,required=True,min_length=2)
    last_name = forms.CharField(max_length=30,required=False)
    contact_no = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(max_length=60,required=True)
    is_tutor = forms.BooleanField(required=False)

    