from django.contrib import admin
from .models import Files


# Register your models here.
class FilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploadfile', 'created_at', 'user')
    list_display_links = ('title', 'uploadfile')
    search_fields = ('title',)
    list_filter = ('title',)


admin.site.register(Files, FilesAdmin)
