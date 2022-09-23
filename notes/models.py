from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.tag

    def __repr__(self) -> str:
        return self.tag

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Note(models.Model):
    name = models.CharField(max_length=40, null=False, unique=True)
    text = models.TextField(null=False)
    tags = models.ManyToManyField(Tag, related_name="tags")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('note', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
