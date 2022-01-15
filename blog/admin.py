from django.contrib import admin
from .models import Post, Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Subject, SubjectAdmin)

admin.site.register(Post)

# Register your models here.
