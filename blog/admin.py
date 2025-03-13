from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')  # Fields to display in the list view
    list_filter = ('date_posted', 'author')  # Add filters
    search_fields = ('title', 'content')  # Add search functionality
    ordering = ('-date_posted',)  # Default ordering

# Register your models here.
admin.site.register(Post)