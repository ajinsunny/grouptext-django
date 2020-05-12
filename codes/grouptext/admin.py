from django.contrib import admin
from .models import TextGroup, TextGroupMember, TextQuestion

# Register your models here.
admin.site.register(TextGroup)
admin.site.register(TextGroupMember)
admin.site.register(TextQuestion)
