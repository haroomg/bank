from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.contrib.auth.hashers import make_password, check_password

# --------------------------------------------------------------------------------
# User:

class TypeUser(models.Model): 
    # Model that represents a type of user in the system.
    
    # Field that stores the type of user name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the type of user description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the type of user creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the type of user last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the type of user is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'customers_type_users'  # Table name in the database
        verbose_name = 'type_user'
        verbose_name_plural = 'type_users'
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the type user name as a string


class StatusUser(models.Model):
    # Model that represents a Status of user in the system.
    
    # Field that stores the status of user name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the status of user description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the status of user creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the status of user last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the status of user is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'customers_status_users'  # Table name in the database
        verbose_name = 'status_user'
        verbose_name_plural = 'status_users'
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the status of user name as a string


class User(models.Model): 
    # Model that represents a user in the system.
    
    # Field that stores the user's type (foreign key to the TypeUser model)
    type_id = models.ForeignKey(TypeUser, on_delete=models.DO_NOTHING)
    
    # Foreign key referencing the status of the user (e.g. active, inactive, etc.)
    status_id = models.ForeignKey(StatusUser, on_delete=models.DO_NOTHING)
    
    # Field that stores the user's username (max 50 characters, unique)
    user_name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    # Field that stores the user's first name (max 50 characters)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    
    # Field that stores the user's last name (max 50 characters)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    
    # Field that stores the user's email (max 50 characters, unique)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    
    # Field that stores the user's phone number (max 50 characters, unique)
    phone = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    # Field that stores the user's identification number (max 50 characters, unique)
    ci = models.CharField(max_length=50, blank=False, null=False, unique=True)
    
    # Field that stores the user's password (max 200 characters)
    password = models.CharField(max_length=200, blank=False, null=False)
    
    # Field that stores the user's address (max 50 characters)
    address = models.CharField(max_length=50, blank=False, null=False)
    
    # Field that stores the user's birthdate
    birthdate = models.DateField(blank=False, null=False)
    
    # Field that stores the user's creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # field that records the time in which the user will be blocked
    blocking_time = models.DateTimeField(blank=True, null=True)
    
    # Field that stores the user's last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that stores the user's password expiration date (6 months from creation)
    date_due_password = models.DateTimeField(default=datetime.now() + relativedelta(months=6))
    
    
    def set_password(self, raw_password):
        # Method that sets the user's password.
        self.password = make_password(raw_password)
        
    def valid_password(self, raw_password):
        # Method that checks if the provided password is valid.
        return check_password(raw_password, self.password)
    
    def is_password_expired(self):
        # Method that checks if the user's password has expired.        
        return self.date_due_password >= timezone.now().date()
    
    def block(self):
        # Method that block an user when for 3 days
        if self.blocking_time != None:
            self.blocking_time = datetime.now() + timedelta(days=3)
    
    def unlock(self):
        # Method that unlock an user
        if self.blocking_time >= timezone.now().date():
            self.blocking_time = None
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.user_name  # Returns the user's username as a string
    
    class Meta:
        # Model metadata.
        db_table = 'customers_users'  # Table name in the database
        verbose_name = 'user'
        verbose_name_plural = 'users'

# --------------------------------------------------------------------------------
# requests
