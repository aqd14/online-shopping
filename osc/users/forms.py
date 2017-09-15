'''
Created on Sep 13, 2017

@author: doquocanh-macbook
'''
from django import forms

class RegistrationForm(forms.Form):
    """Registration form fields
    
    """
    username = forms.CharField()
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')
    
class LoginForm(forms.Form):
    """Login by entering email and password
    
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)