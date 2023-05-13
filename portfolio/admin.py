from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Projects)
admin.site.register(Tag)
admin.site.register(Skills)
admin.site.register(Messages)
admin.site.register(Comments)