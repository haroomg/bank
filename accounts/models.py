from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
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
        db_table = 'type_users'  # Table name in the database
    
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
        db_table = 'status_user'  # Table name in the database
    
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
    
    # Field that indicates if the user is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
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
        db_table = 'users'  # Table name in the database

# --------------------------------------------------------------------------------
# Account
class StatusAccount(models.Model): 
    # Model that represents the status of an account in the system.
    
    # Field that stores the status name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the status description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the status creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the status last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the status is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'status_account'  # Table name in the database
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the status name as a string


class TypeAccount(models.Model): 
    # Model that represents a Type of Account in the system.
    
    # Field that stores the type of account name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the type of account description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the type of account creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the type of account last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the type of account is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'type_account'  # Table name in the database
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the type of account name as a string


class Account(models.Model): 
    # Represents a bank account associated with a user.
    
    # Foreign key referencing the user who owns this account
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    # Foreign key referencing the type of account (e.g. checking, savings, etc.)
    type_id = models.ForeignKey(TypeAccount, on_delete=models.DO_NOTHING)
    
    # Foreign key referencing the status of the account (e.g. active, inactive, etc.)
    status_id = models.ForeignKey(StatusAccount, on_delete=models.DO_NOTHING)
    
    # Unique account number assigned to the account
    account_number = models.CharField(max_length=50, blank=False, null=False)
    
    # Current balance of the account
    balance = models.FloatField(default=0)
    
    # field that records the time in which the user will be blocked
    blocking_time = models.DateTimeField(blank=True, null=True)
    
    # Timestamp when the account was created
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Timestamp when the account was last updated
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Database table name for this model
        db_table = 'accounts'
    
    def block(self):
        # Method that block an user when for 3 days
        if self.blocking_time != None:
            self.blocking_time = datetime.now() + timedelta(days=3)
    
    def unlock(self):
        # Method that unlock an user
        if self.blocking_time >= timezone.now().date():
            self.blocking_time = None
    
    def __str__(self):
        # Returns a string representation of the account
        return f"{self.user_id.user_name} - {self.account_number}"

# --------------------------------------------------------------------------------
# Card

class TypeCard(models.Model): 
    # Model that represents a type of card in the system.
    
    # Field that stores the type of card name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the type of card description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the type of card creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the type of card last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the type of card is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'type_card'  # Table name in the database
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the type of card name as a string


class StatusCard(models.Model): 
    # Model that represents the status of a card in the system.
    
    # Field that stores the status name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the status description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the status creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the status last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the status is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'tatus_card'  # Table name in the database
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the status name as a string


class Card(models.Model): 
    # Represents a bank card associated with an account.
    
    # Foreign key referencing the account that this card belongs to
    account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    
    # Foreign key referencing the type of card (e.g. credit, debit, etc.)
    type_id = models.ForeignKey(TypeCard, on_delete=models.DO_NOTHING)
    
    # Foreign key referencing the status of the card (e.g. active, inactive, etc.)
    status_id = models.ForeignKey(StatusCard, on_delete=models.DO_NOTHING)
    
    # Unique card number assigned to the card
    card_number = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Reference number associated with the card
    ref = models.CharField(max_length=30, blank=False, null=False, unique=True)
    
    # Password associated with the card (hashed for security)
    password_card = models.CharField(max_length=6, blank=False, null=False)
    
    # Date when the card password is due to expire
    date_due_password = models.DateTimeField(default=datetime.now() + relativedelta(months=6))
    
    # field that records the time in which the user will be blocked
    blocking_time = models.DateTimeField(blank=True, null=True)
    
    # Timestamp when the card was created
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Timestamp when the card was last updated
    date_update = models.DateTimeField(auto_now=True)
    
    def block(self):
        # Method that block an account when for 3 days
        if self.blocking_time != None:
            self.blocking_time = datetime.now() + timedelta(days=3)
    
    def unlock(self):
        # Method that unlock an account
        if self.blocking_time >= timezone.now().date():
            self.blocking_time = None
    
    def __str__(self):
        # Returns a string representation of the account
        return f"{self.account_id.user_id.user_name} - {self.account_number}"

# --------------------------------------------------------------------------------
# POS

class TypePos(models.Model): 
    # Model that represents a type of point sale in the system.
    
    # Field that stores the type of point sale name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the type of point sale description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the type of point sale creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the type of point sale last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the type of point sale is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'type_'  # Table name in the database
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the type of card name as a string


class StatusPos(models.Model): 
    # Model that represents the status of a point of sale in the system.
    
    # Field that stores the status name (max 20 characters)
    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # Field that stores the status description (max 255 characters)
    description = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Field that stores the status creation date
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Field that stores the status last update date
    date_update = models.DateTimeField(auto_now=True)
    
    # Field that indicates if the status is active (True) or inactive (False)
    status = models.BooleanField(default=True)
    
    class Meta:
        # Model metadata.
        db_table = 'status_point_sale'  # Table name in the database
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the status name as a string


class PointSale(models.Model): 
    # Represents a point of sale (POS) associated with an account.

    # Foreign key referencing the account that this POS belongs to
    account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    
    # Foreign key referencing the type of POS (e.g. credit, debit, etc.)
    type_id = models.ForeignKey(TypePos, on_delete=models.DO_NOTHING)
    
    # Foreign key referencing the status of the POS (e.g. active, inactive, etc.)
    status_id = models.ForeignKey(StatusPos, on_delete=models.DO_NOTHING)
    
    # Unique identifier for the POS
    point_sale_number = models.CharField(max_length=20, blank=False, null=False, unique=True)
    
    # field that records the time in which the user will be blocked
    blocking_time = models.DateTimeField(blank=True, null=True)
    
    # Timestamp when the POS was created
    date_create = models.DateTimeField(auto_now_add=True)
    
    # Timestamp when the POS was last updated
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta: 
        # Database table name for this model
        db_table = 'point_sales'
    
    def block(self):
        # Method that block an point sale when for 3 days
        if self.blocking_time != None:
            self.blocking_time = datetime.now() + timedelta(days=3)
    
    def unlock(self):
        # Method that unlock an point sale
        if self.blocking_time >= timezone.now().date():
            self.blocking_time = None
    
    def __str__(self):
        # Returns a string representation of the POS
        return f"{self.account_id.user_id.user_name} - {self.point_sale_number}"

# --------------------------------------------------------------------------------
