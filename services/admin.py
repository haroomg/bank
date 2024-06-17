from django.contrib import admin
from .models import (
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