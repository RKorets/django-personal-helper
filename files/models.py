from django.db import models
from django.contrib.auth.models import User
from .file_ext_valid import ContentTypeRestrictedFileField


def directory_path(instance, filename):
    return f'upload_files/{instance.user.pk}/{filename}'


class Files(models.Model):
    title = models.CharField(max_length=200)
    uploadfile = ContentTypeRestrictedFileField(upload_to=directory_path, verbose_name='Files', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date_file')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Files"
        verbose_name_plural = "Files"
        ordering = ['-created_at']
