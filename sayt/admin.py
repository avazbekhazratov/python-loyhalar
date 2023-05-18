from django.contrib import admin
from .models import News, Category, Contact, Comments

# Register your models here.

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Contact)
admin.site.register(Comments)

