from django.contrib import admin
from .models import Issue

# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_link', 'issue_link','created_at')
    search_fields = ['title']

admin.site.register(Issue, IssueAdmin)