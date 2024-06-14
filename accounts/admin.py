from django.contrib import admin
from .models import (
    # user
    StatusUser,
    TypeUser,
    User,
    
    # account
    StatusAccount,
    TypeAccount,
    Account,
    
    # card
    StatusCard,
    TypeCard, 
    Card,
    
    # pos
    StatusPos,
    TypePos,
    Pos
)

# uses
admin.site.register(StatusUser)
admin.site.register(TypeUser)
admin.site.register(User)

# account
admin.site.register(StatusAccount)
admin.site.register(TypeAccount)
admin.site.register(Account)

# card
admin.site.register(StatusCard)
admin.site.register(TypeCard)
admin.site.register(Card)

# pos
admin.site.register(StatusPos)
admin.site.register(TypePos)
admin.site.register(Pos)