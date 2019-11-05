from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Chair)

admin.site.register(Table)