from django.db import models

from validate_email import validate_email

class Customer(models.Model):
    """Customer model 
    """
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    confirm_pw = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    # birthday = models.DateField(null=True, blank=True)
    # address = models.CharField(max_length=100, required=False)
    
    def is_valid_email(self):
        """Check if entered email is valid or not
        """
        return validate_email(self.email)
    
    def validate_password(self):
        return self.password == self.confirm_pw
    
    def __str__(self):
        return 'Username: ' + self.username + '\nEmail: ' + self.email
    
    def is_valid(self):
        return True
    