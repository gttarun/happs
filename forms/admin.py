from django.contrib import admin
from .models import User, invitees
# Register your models here.
admin.site.register(User)
admin.site.register(invitees)
