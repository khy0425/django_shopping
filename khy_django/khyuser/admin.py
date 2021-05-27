from django.contrib import admin
from .models import Khyuser
# Register your models here.

class KhyuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

admin.site.register(Khyuser, KhyuserAdmin)