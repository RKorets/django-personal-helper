from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


class Contacts(models.Model):
    name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    phone_one = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=55, blank=True, null=True)
    email_one = models.EmailField(max_length=55, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def get_absolute_url(self):
        return reverse('contact', kwargs={'pk': self.pk})

    def days_to_birthday(self):
        if self.birthday is None:
            return 'date is empty'
        contact_birthday_month = self.birthday.month
        contact_birthday_day = self.birthday.day
        if date.today().month >= contact_birthday_month:
            if date.today().month == contact_birthday_month and date.today().day > contact_birthday_day:
                current_year_birthday = date(year=date.today().year+1, month=self.birthday.month, day=self.birthday.day)

            else:
                current_year_birthday = date(year=date.today().year, month=self.birthday.month, day=self.birthday.day)
        else:
            current_year_birthday = date(year=date.today().year, month=self.birthday.month, day=self.birthday.day)
        birthday = current_year_birthday - date.today()
        if birthday.days == 0:
            return 'Today'

        return abs(birthday.days)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
