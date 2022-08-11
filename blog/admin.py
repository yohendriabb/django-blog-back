from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display= ('blog_uuid', 'title', 'slug', 'thumbnail', 'video', 'description', 'execerpt', 'category', 'published', 'status')
admin.site.register(Post, PostAdmin)
