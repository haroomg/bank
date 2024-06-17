from django.db import models
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.utils.module_loading import import_module

account_models = import_module('customers.models')
User = account_models.User

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
        db_table = 'services_status_account'  # Table name in the database
        verbose_name = 'status_user'
        verbose_name_plural = 'status_users'
    
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
        db_table = 'services_type_account'  # Table name in the database
        verbose_name = 'type_account'
        verbose_name_plural = 'type_accounts'
    
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
        
        db_table = 'services_accounts' # Database table name for this model
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
    
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
        db_table = 'services_type_cards'  # Table name in the database
        verbose_name = 'type_card'
        verbose_name_plural = 'type_cards'
    
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
        db_table = 'services_status_cards'  # Table name in the database
        verbose_name = 'status_card'
        verbose_name_plural = 'status_cards'
    
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
    
    class Meta:
        # Model metadata.
        db_table = 'services_cards'  # Table name in the database
        verbose_name = 'card'
        verbose_name_plural = 'cards'

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
        db_table = 'services_type_pos'  # Table name in the database
        verbose_name = 'pos'
        verbose_name_plural = 'pos'
    
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
        db_table = 'services_status_pos'  # Table name in the database
        verbose_name = 'status_pos'
        verbose_name_plural = 'status_pos'
    
    def __str__(self):
        # Method that returns a string representation of the object.
        return self.name  # Returns the status name as a string


class Pos(models.Model): 
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
        db_table = 'services_pos'
        verbose_name = 'status_pos'
        verbose_name_plural = 'status_pos'
    
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