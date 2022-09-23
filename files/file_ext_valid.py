from django.db.models import FileField
from django.forms import forms

content_types = ['application/msword',
                 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                 'image/jpeg', 'image/png', 'application/pdf', 'text/plain', ]


class ContentTypeRestrictedFileField(FileField):
    def __init__(self, *args, **kwargs):
        self.content_types = content_types

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        try:
            content_type = file.content_type
            if content_type not in self.content_types:
                raise forms.ValidationError('Invalid file extension.')
        except AttributeError:
            pass

        return data


# def validate_file_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
#     valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
#     if not ext.lower() in valid_extensions:
#         raise ValidationError('Unsupported file extension.')
