from django.contrib import admin
from . models import News, SportNews, DataRegistro, Post

# Register your models here.
admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(DataRegistro)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'author', 'slug', 'update', 'created')
    prepopulated_fields = {'slug': ('title',)}
