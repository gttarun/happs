from django.contrib import admin
from .models import UserEvents, FileUpload

admin.site.register(UserEvents)
admin.site.register(FileUpload)
