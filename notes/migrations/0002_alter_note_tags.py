# Generated by Django 3.2.15 on 2022-09-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='notes.Tag'),
        ),
    ]