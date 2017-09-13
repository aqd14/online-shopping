from django.db import models
from django import forms

from validate_email import validate_email
from material import Layout, Row, Fieldset

class User(models.Model):
    """User model
    
    Parameters
    ----------
    """
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    confirm_pw = models.CharField(max_length=30)
    email = models.EmailField()
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100)
    
    def is_valid_email(self):
        """Check if entered email is valid or not
        """
        return validate_email(self.email)
    
    def validate_password(self):
        return self.password == self.confirm_pw
    
    def __str__(self):
        return 'Username: ' + self.username + '\nEmail: ' + self.email
    
class RegistrationForm(forms.Form):
    """Registration form attributes
    
    """
    username = forms.CharField()
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')))
    receive_news = forms.BooleanField(required=False, label='I want to receive news and special offers')
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password', 'password_confirm'),
                    Fieldset('Pesonal details',
                        Row('first_name', 'last_name'),
                            'gender', 'receive_news', 'agree_toc'))
    
    def is_valid(self):
        return True
    