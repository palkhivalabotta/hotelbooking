from django.contrib import admin

from .models import UserRegister
from .models import availablerooms
from .models import amount
from .models import card




admin.site.register(UserRegister)
admin.site.register(availablerooms)
admin.site.register(amount)
admin.site.register(card)
