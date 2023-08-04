from django.contrib import admin
from blogapp.models import Post

class BlogAdmin(admin.ModelAdmin):
   list_display = ['title', 'body', 'headline', 'image']
   prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, BlogAdmin)