from django.contrib import admin
from .models import Notice
# Register your models here.

# admin.site.register(Notice)
@admin.register(Notice)
class Notice(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'date_post')

