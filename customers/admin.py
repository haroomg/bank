from django.contrib import admin

from django.contrib import admin
from .models import (
    # user
    StatusUser,
    TypeUser,
    User,
    
)

# uses
admin.site.register(StatusUser)
admin.site.register(TypeUser)
admin.site.register(User)